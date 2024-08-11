from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.http import HttpResponse
from django.views import generic
from .models import Client, Note
from django.contrib.auth.decorators import login_required



# Create your views here.
# def home(request):
#    return render(request, 'cms/home.html')

def home(request):
    return render(request, 'cms/home.html')



# Create the form class.
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "gender", "birth_date", "address", "phone_number", "condition"]

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "slug", "author", "content"]

# Define the contents of the note content view
def note_content(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'cms/note_content.html', {'note': note})

# Define the adding of notes
@login_required
def note_create(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_content', pk=form.instance.pk)
    else:
        form = NoteForm()
    return render(request, 'cms/note_edit.html', {'form': form})
    
    # if request.method == 'POST':
    #     # Manually create the note fields
    #     note.title = request.POST.get('title', '')
    #     note.slug = request.POST.get('slug', '')
    #     note.content = request.POST.get('content', '')
        
    #     # Save the note
    #     note.save()
        
    #     # Redirect to the note detail page
    #     return HttpResponseRedirect(reverse('note_content', args=[pk]))
    
    # # Render the edit form with the new note's data
    # return render(request, 'cms/note_edit.html', {'note': note})


# Define the editing of notes
@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == 'POST':
        # Manually update the note fields
        note.title = request.POST.get('title', '')
        note.slug = request.POST.get('slug', '')
        note.content = request.POST.get('content', '')
        
        # Save the note
        note.save()
        
        # Redirect to the note detail page
        return HttpResponseRedirect(reverse('note_content', args=[pk]))
    
    # Render the edit form with the current note's data
    return render(request, 'cms/note_edit.html', {'note': note})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    # Ensure the user has the correct permissions
    if hasattr(request.user, 'client') and request.user.client.id == pk:
        # The user is the client themselves, deny edit access, only view
        return render(request, 'cms/error.html', {'error_message': 'Clients cannot delete their own notes.'})
    elif hasattr(request.user, 'carer') and request.user.carer.clients.filter(pk=pk).exists():
        # The user is not a carer for this client, deny editing
        messages.error(request, 'Carers cannot delete notes of clients they do not manage. Please contact an administrator if this note needs to be removed.')
        return redirect('client_detail')
    
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed', False) == 'true'
        if confirmed:
            note.delete()
            messages.success(request, 'Note deleted!')
            return redirect('client_list')
        else:
            messages.info(request, 'Note deletion cancelled.')
            return redirect('client_list')
    else:
        messages.error(request, 'Only carers can delete notes.')
        return redirect('client_detail')



@login_required
def client_list(request):
    """
    Return list of clients if authenticated user
    **Context**
    ``Client``
        All instances of :model: Client`.
    """
    if request.method == "GET":
        query = request.GET.get('q')
        clients = Client.objects.all()

        if query:
            # Filter clients based on the query and check if the user is the client or a carer
            clients = clients.filter(first_name__icontains=query)

        # Further filter the clients based on the user's relationship
        if request.user.is_authenticated:
            # If the user is a Client
            if hasattr(request.user, 'client'):
                clients = clients.filter(id=request.user.client.id)
            # If the user is a Carer
            elif hasattr(request.user, 'carer'):
                clients = clients.filter(carers=request.user.carer)
            else:
                # If the user is not a client or carer, restrict access 
                clients = Client.objects.none() 
                #update for error page
                return render(request, 'cms/') #Update for error page


        return render(request, 'cms/client_list.html', {'clients': clients})

@login_required
def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cms:client_list')  # Redirect to the list of patients after saving
    else:
        form = ClientForm()

    return render(request, 'cms/add_client.html', {'form': form})

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    # Ensure the user has the correct permissions
    if hasattr(request.user, 'client') and request.user.client.id == pk:
        # The user is the client themselves, deny edit access, only view
        return render(request, 'cms/error.html', {'error_message': 'You do not have permission to edit this client.'})
    elif hasattr(request.user, 'carer') and request.user.carer.clients.filter(pk=pk).exists():
        # The user is a carer for this client, allow editing
        if request.method == "POST":
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():
                form.save()
                return redirect('cms:client_list')
        else:
            form = ClientForm(instance=client)
        return render(request, 'cms/client_form.html', {'form': form})
    else:
        # The user is neither the client nor a carer associated with the client
        return render(request, 'cms/error.html', {'error_message': 'You do not have permission to edit this client.'})

@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    # Ensure the user has the correct permissions
    if hasattr(request.user, 'carer') and request.user.carer.clients.filter(pk=pk).exists():
        # The user is a carer for this client, allow deletion
        client.delete()
        return redirect('cms:client_list')
    else:
        # The user is not a carer associated with the client, deny deletion
        return render(request, 'cms/error.html', {'error_message': 'You do not have permission to delete this client.'})

@login_required
def client_detail(request, pk):
    # Fetch the client object, or return a 404 if it doesn't exist
    client = get_object_or_404(Client, pk=pk)
    notes = client.notes.all()

    # Check if the user has permission to view the client
    if request.user.is_authenticated:
        if hasattr(request.user, 'client') and request.user.client.id == pk:
            pass  # The user is the client, so they are allowed to view the details
        elif hasattr(request.user, 'carer') and request.user.carer.clients.filter(pk=pk).exists():
            pass  # The user is a carer for this client, so they are allowed to view the details
        else:
            # The user is neither the specific client nor a carer associated with the client
            return render(request, 'cms/error.html', {'error_message': 'You do not have permission to view this client.'})

    # Determine if the user is allowed to edit/delete notes
    carer_for_client = False
    if hasattr(request.user, 'carer') and request.user.carer.clients.filter(pk=pk).exists():
        carer_for_client = True

    context = {
        'client': client,
        'notes': notes,
        'carer_for_client': carer_for_client,
    }

    # Render the client detail page with the appropriate context
    return render(request, 'cms/client_detail.html', context)