from django.contrib import admin
from .models import Client, Carer, Note

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'birth_date', 'address', 'phone_number')
    search_fields = ('first_name', 'last_name', 'address', 'phone_number')
    list_filter = ('gender',)

class CarerAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username',)
    filter_horizontal = ('clients',)

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on',)
    search_fields = ('title', 'author__username', 'client__first_name', 'client__last_name')
    list_filter = ('author', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    # filter_horizontal = ('clients',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Carer, CarerAdmin)
admin.site.register(Note, NoteAdmin)

