from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Mascota, Estado

admin.site.site_header = "Mantendeor MisPerris"


class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id_mascota', 'nom_mascota', 'tamano_mascota','peso_mascota','color_mascota','fecha_rescate','descripcion','estado')
    list_filter = ('estado',)
    ordering = ('id_mascota',)
    search_fields = ('nom_mascota',)

admin.site.register(Estado)
admin.site.register(Mascota,RegistroAdmin)




