from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from bases.models import *
from .forms import ContactoForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse

from django.http import JsonResponse
# from rest_framework.response import Response
from django.db.models import Q

# Create your views here.

def send_user_mail(request, pk):
    correo = get_object_or_404(Emprendedor, pk=pk)
    e = Emprendedor.objects.get(email=correo.email)
    
    if request.method=='POST':
        subject=request.POST['asunto']
        nombre=request.POST['nombre']
        telef=request.POST['telefono']
        
        message=request.POST['mensaje']+"\n" + "\nRemitente:\n"+nombre+"\n\nEmail: \n"+request.POST['email']+"\n\nTeléfono: \n"+telef
        
        email_form = settings.EMAIL_HOST_USER
        
        if subject and message and email_form:
            try:
                send_mail(subject, message, email_form, [e])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        # recipient_list=['cristianfroning@gmail.com']
        # send_mail(subject, message, email_form, recipient_list)
        return render (request, 'bases/mensaje_enviado.html')

    return render(request, 'bases/contacto.html')

# este será reeemplazo de la funcion listado_emprendimientos
def listado_categorias(request):
    busqueda = request.GET.get("buscar")
# presentacion de todas las cat existentes
    lista_categ=Categoria.objects.all()
# paginación
    paginator=Paginator(lista_categ, 15)
    pagina=request.GET.get("page") or 1
    categ=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1, categ.paginator.num_pages +1)

    if busqueda:
        categ = Categoria.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()

    return render(request, 'bases/listado_categorias.html', {'categ':categ, 'paginas':paginas, 'pagina_actual':pagina_actual})

def autosuggest(request):
    # print(request.GET)
    busque = request.GET.get('term')
    print(busque)
    queryset = Categoria.objects.filter(nombre__icontains=busque)
    mylist = []
    mylist += [x.nombre for x in queryset]
    return JsonResponse(mylist, safe=False)

def listado_categorias_buscar(request):
    busqueda = request.GET.get("buscar")
    queryset = Categoria.objects.filter(
        Q(nombre__icontains=busqueda) |
        Q(descripcion__icontains=busqueda)
    ).distinct()
    mylist = []
    mylist += [x.nombre for x in queryset]
    return JsonResponse(mylist, safe=False)

# ---------------------------------------------------- FUNCIONES PARA EMPRENDIMIENTOS -----------------------------------------------------

def lista_emprendimientos_categoria(request, pk):
    busqueda = request.GET.get("buscar")
# listado de los emprendimientos por categoria seleccionada
    cat = get_object_or_404(Categoria, pk=pk)
    lista_emprendimientos = Emprendimiento.objects.filter(categoria=cat)
# paginación
    paginator=Paginator(lista_emprendimientos, 10)
    pagina=request.GET.get("page") or 1
    emprendimientos=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1, emprendimientos.paginator.num_pages +1)
    
    
    if busqueda:
        emprendimientos = Emprendimiento.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(descripcion__icontains = busqueda)
        ).distinct()

    return render(request, 'bases/listado_emprendimiento.html', {'emprendimientos':emprendimientos, 'paginas':paginas, 'pagina_actual':pagina_actual})

def lista_productos_emprendimiento(request, pk):
    # presentamos los productos por medio del filtro
    emprend = get_object_or_404(Emprendimiento, pk=pk)
    lista_productos = Producto.objects.filter(emprendimiento=emprend)
    empddr= emprend.emprendedores.all()
    paginator=Paginator(lista_productos, 10)
    pagina=request.GET.get("page") or 1
    productos=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1, productos.paginator.num_pages +1)

    busqueda = request.GET.get("buscar")
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        ).distinct()

    return render(request, 'bases/listado_productos.html', {'productos':productos, 'emp':empddr, 'pagina_actual':pagina_actual, 'paginas':paginas})


def autocomplete(request):
    # print(request.GET)
    busquepro = request.GET.get('termpro')
    print(busquepro)
    queryset = Producto.objects.filter(nombre__icontains=busquepro)
    mylist = []
    mylist += [x.nombre for x in queryset]
    return JsonResponse(mylist, safe=False)


def listado_productos_buscar(request):
    busqueda = request.GET.get("buscar")
    queryset = Producto.objects.filter(
        Q(nombre__icontains=busqueda) |
        Q(descripcion__icontains=busqueda)
    ).distinct()
    mylist = []
    mylist += [x.nombre for x in queryset]
    return JsonResponse(mylist, safe=False)
 


# ------------------------------------------------ para listar propietarios de cada emprendimiento -----------------------------------------

def lista_propietarios(request, pk):
    # presentamos los productos por medio del filtro
    emprend = get_object_or_404(Emprendimiento, pk=pk)
    # lista_productos = Producto.objects.filter(emprendimiento=emprend)
    empddr= emprend.emprendedores.all()
    
    return render(request, 'bases/propietarios.html', {'emp':empddr})


#---------------------------------------------------------- apartado para la función de contacto-municipio-----------------------------------------------
# def mensaje_enviado(request):
#     return render(request, 'bases/mensaje_enviado.html')

def contacto_municipio(request):
    if request.method=='POST':
        correo=request.POST['email']
        nombre=request.POST['nombre']
        telef=request.POST['telefono']
        subject=request.POST['asunto']
        message=request.POST['mensaje']+" | Remitente: "+nombre+" email: "+ correo+" teléfono: "+telef
        email_form = settings.EMAIL_HOST_USER
        recipient_list=['emprendimientosquilanga@gmail.com']
        send_mail(subject, message, email_form, recipient_list)
        
        return render (request, 'bases/mensaje_enviado.html')
    return render(request, 'bases/contacto.html')

# ----------------------------------------------------PAGINA NO ENCONTRADA--------------------------------------------------- #
# from django.template import RequestContext
# from django.shortcuts import render_to_response

def mi_error_404(request, exception):
    return render(request, 'bases/404.html')


