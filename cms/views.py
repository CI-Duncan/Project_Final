from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .forms import ClientForm, NoteForm 
from .models import Client, Note
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)



# Create your views here.
def home(request):
    return render(request, 'cms/home.html')

# Note list view
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'cms/note_list.html', {'notes': notes})

# Note content view
def note_content(request, pk):
    note = get_object_or_404(Note, pk=pk)
    # form = NoteForm()
    return render(request, 'cms/note_content.html', {'note': note})

# Adding of notes
    """
    Create an individual note :model:`cms.Note`.

    **Context**

    ``Note``
        An instance of :model:`cms.Note`.

    **Template:**

    :template:`cms/note_create.html`
    """
@login_required
def note_create(request, pk):
    client = get_object_or_404(Client, pk=pk)  # Fetch the client using the primary key (pk)
    
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.client = client  # Associate the note with the fetched client
            note.author = request.user  # Automatically set the author as the logged-in user (carer)
            try:
                note.save()
                logger.info(f"Saved note with slug: {note.slug}")
                messages.add_message(
                request, messages.SUCCESS,
                f'Note created for {client.first_name} {client.last_name}.'
                )
                return redirect('cms:note_content', pk=note.pk)  # Redirect to the newly created note's content page
            except Exception as e:
                logger.error(f"Failed to save note: {e}")
                messages.error(request, 'Failed to save note. Please try again.')
        else:
            logger.warning("Form is not valid")
            messages.warning(request, 'Form validation failed. Please correct the errors and try again.')
    else:
        form = NoteForm()
    
    return render(request, 'cms/note_create.html', {'client': client, 'form': form})

# Editing of notes
    """
    Edits an individual note :model:`cms.Note`.

    **Context**

    ``Note``
        An instance of :model:`cms.Note`.

    **Template:**

    :template:`cms/note_edit.html`
    """
@login_required
def note_edit(request, pk):
    # Fetch the note object using the primary key (pk)
    note = get_object_or_404(Note, pk=pk)
    
    if request.method == 'POST':
        # Bind the form to the POST data and the existing note instance
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully.')
            return redirect('cms:note_content', pk=note.pk)  # Redirect to the note content page after successful edit
        else:
            # Log or handle form validation errors
            logger.warning("Form validation failed for note edit.")
            messages.warning(request, 'Form validation failed. Please correct the errors and try again.')
    else:
        # If GET request, instantiate the form with the existing note instance
        form = NoteForm(instance=note)
    
    # Render the note edit template with the form
    return render(request, 'cms/note_edit.html', {'form': form})

# Deleting notes
    """
    Deletes an individual note :model:`cms.Note`.

    **Context**

    ``Note``
        An instance of :model:`cms.Note`.

    **Template:**

    Handled by JavaScript
    """
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    client = note.client  # Get the associated client for the note

    # Ensure the user has the correct permissions
    if hasattr(request.user, 'client') and request.user.client.id == pk:
        # The user is the client themselves, deny edit access, only view
        return render(request, 'cms/error.html', {'error_message': 'Clients cannot delete their own notes.'})
    elif hasattr(request.user, 'carer') and request.user.carer.clients.filter(pk=pk).exists():
        # The user is not a carer for this client, deny editing
        messages.error(request, 'Carers cannot delete notes of clients they do not manage. Please contact an administrator if this note needs to be removed.')
        return redirect('cms:client_detail', pk=client.pk)
    
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed', False) == 'true'
        if confirmed:
            note.delete()
            messages.success(request, 'Note deleted!')
            return redirect('cms:client_list')
        else:
            messages.info(request, 'Note deletion cancelled.')
            return redirect('cms:client_list')
    else:
        messages.error(request, 'Only carers can delete notes.')
        return redirect('cms:client_detail', pk=client.pk)

# List of clients
    """
    Return list of clients if authenticated user

    **Context**

    ``Note``
        An instance of :model:`cms.Client`.

    **Template:**

    :template:`cms/client_list.html`
    """
@login_required
def client_list(request):
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

# Add new client
    """
    Creates a new clients if authenticated user

    **Context**

    ``Note``
        An instance of :model:`cms.Client`.

    **Template:**

    :template:`cms/add_client.html`
    """
@login_required
def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cms:client_list')
    else:
        form = ClientForm()
    return render(request, 'cms/add_client.html', {'form': form})

# Edit client
    """
    Edits an existing client if authenticated user

    **Context**

    ``Note``
        An instance of :model:`cms.Client`.

    **Template:**

    :template:`cms/client_form.html`
    """
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
                messages.add_message(
                    request, messages.SUCCESS,
                    f'{client.first_name} {client.last_name} has been successfully updated.'
                )
                return redirect('cms:client_list')
        else:
            form = ClientForm(instance=client)
        return render(request, 'cms/client_form.html', {'form': form})
    else:
        # The user is neither the client nor a carer associated with the client
        return render(request, 'cms/error.html', {'error_message': 'You do not have permission to edit this client.'})

# Delete client
    """
    Deletes an existing client if authenticated user

    **Context**

    ``Note``
        An instance of :model:`cms.Client`.

    **Template:**

    :template:`**`
    """
@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    # Ensure the user has the correct permissions
    if hasattr(request.user, 'carer') and request.user.carer.clients.filter(pk=pk).exists():
        if request.method == 'POST':
            # The user confirmed deletion, so delete the client
            client_name = f"{client.first_name} {client.last_name}"
            client.delete()
            # Add success message with the client's name
            messages.add_message(
                request, messages.SUCCESS,
                f'Client {client_name} has been successfully deleted.'
            )
            return redirect('cms:client_list')
        else:
            # Render a confirmation page before deletion
            return render(request, 'cms/client_confirm_delete.html', {'client': client})
    else:
        # The user is not a carer associated with the client, deny deletion
        return render(request, 'cms/error.html', {'error_message': 'You do not have permission to delete this client.'})

# Detail view for a client
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