from django.contrib import admin
from bases.models import *

# Register your models here.

class EmprendedorAdmin(admin.ModelAdmin):
    list_display=["cedula", "nombres", "apellidos", "direccion", "email", "tfno", "imagen", "facebook", "twitter", "instagram", "whatsapp"]
    list_display_links=["cedula"]
    search_fields=["cedula", "nombres", "apellidos"]
    list_per_page=10

class EmprendimientoAdmin(admin.ModelAdmin):
    list_display=["nombre", "descripcion", "direccion", "imagen", "fecha_creacion"]
    list_display_links=["nombre"]
    ordering=["id","nombre", "descripcion", "imagen"]
    search_fields=["nombre"]
    list_per_page=10

class CategoriaAdmin(admin.ModelAdmin):
    list_display=["nombre", "descripcion", "imagen"]
    search_fields=["nombre"]
    list_per_page=10

class ProductoAdmin(admin.ModelAdmin):
    list_display=["codigo", "nombre", "marca", "descripcion", "precio", "emprendimiento", "imagen"]
    list_display_links=["codigo","nombre"]
    search_fields=["codigo", "nombre", "marca"]
    list_filter=["marca"]
    list_per_page=10

class ContactoAdmin(admin.ModelAdmin):
    list_display=["asunto","nombre","email","telefono","mensaje"]

admin.site.register(Emprendedor, EmprendedorAdmin)
admin.site.register(Emprendimiento, EmprendimientoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto, ContactoAdmin)
