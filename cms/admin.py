from django.contrib import admin
from .models import Client, Carer, Note
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ClientAdmin(SummernoteModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'birth_date', 'address', 'phone_number',)
    search_fields = ('first_name', 'last_name', 'address', 'phone_number',)
    list_filter = ('gender',)

class CarerAdmin(SummernoteModelAdmin):
    list_display = ('user', 'role',)
    search_fields = ('user__username',)
    filter_horizontal = ('clients',)

@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on',)
    search_fields = ('title', 'author__username', 'client__first_name', 'client__last_name',)
    list_filter = ('author', 'created_on', 'client',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
   


admin.site.register(Client, ClientAdmin)
admin.site.register(Carer, CarerAdmin)


