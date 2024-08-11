from django import forms
from .models import Client, Note

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "gender", "birth_date", "address", "phone_number", "condition"]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "author", "content"]