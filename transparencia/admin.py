from django.contrib import admin
from .models import Servidor

class ServidorAdmin(admin.ModelAdmin):
	list_display = ['nome_servidor', 'categoria', 'caminho', 'setor']
	search_fields = ['nome_servidor', 'cargo', 'caminho', 'setor']
	list_filter = ['unidade', 'categoria']

admin.site.register(Servidor, ServidorAdmin)


