from .models import Client, Note
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "gender", "birth_date", "address",
                  "phone_number", "condition"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", ]
