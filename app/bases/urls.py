from django.urls import path
from bases.views import listado_categorias
from bases.views import lista_emprendimientos_categoria 
from bases.views import lista_productos_emprendimiento 
from bases.views import contacto_municipio 
from bases.views import send_user_mail
from bases.views import lista_propietarios
# PARA CATEGORIAS
from bases.views import autosuggest
from bases.views import listado_categorias_buscar

# PARA EMPRENDIMIENTOS

# PARA PRODUCTOS
from bases.views import autocomplete
from bases.views import listado_productos_buscar

handler404 = 'bases.views.mi_error_404'

urlpatterns = [
    path('', listado_categorias, name="listado_categorias"),
    path('emprendimientos/<int:pk>/', lista_emprendimientos_categoria, name="lista_emprendimientos_categoria"),
    path('productos/<int:pk>/', lista_productos_emprendimiento,name="lista"),
    path('propietarios/<int:pk>/', lista_propietarios,name="propietarios"),
    path('contacto/municipio-quilanga/', contacto_municipio, name="contacto_municipio"),
    path('enviarcorreo-emprendedor/<int:pk>/', send_user_mail, name="enviarcorreo"),
# PARA BUSCAR CATEGORIAS
    path('autosuggest', autosuggest, name="autosuggest"),
    path('listado_categorias_buscar', listado_categorias_buscar, name="listado_categorias_buscar"),

# PARA BUSCAR PRODUCTOS
    path('autocomplete', autocomplete, name="autocomplete"),
    path('listado_productos_buscar', listado_productos_buscar, name="listado_productos_buscar"),
]
