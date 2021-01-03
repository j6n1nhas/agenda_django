from django.contrib import admin
from .models import Categoria, Contacto


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apelido', 'telefone', 'mostrar')
    list_display_links = ('nome', 'apelido', 'telefone')
    list_editable = ('mostrar', )
    search_fields = ['nome', 'apelido', 'telefone']


admin.site.register(Categoria)
admin.site.register(Contacto, ContactoAdmin)