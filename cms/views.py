from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from django.http import HttpResponse
from django.views import generic
from .models import Client, Note



# Create your views here.
# def home(request):
#    return render(request, 'cms/home.html')

def home(request):
    return render(request, 'cms/home.html')



# Create the form class.
class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "gender", "birth_date", "address", "phone_number"]

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["title", "slug", "author", "content"]



def client_list(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(first_name__icontains=query)
    else:
        clients = Client.objects.all()
    return render(request, 'cms/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'cms/client_detail.html', {'client': client})

def client_new(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cms:client_list')  # Redirect to the list of patients after saving
    else:
        form = ClientForm()

    return render(request, 'cms/add_client.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('cms:client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'cms/client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('cms:client_list')