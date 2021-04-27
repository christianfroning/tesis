from django.db import models
# Create your models here.

class Emprendedor(models.Model):
    cedula=models.CharField(max_length=10, verbose_name="cédula", unique=True)
    nombres=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    direccion=models.CharField(max_length=150, verbose_name="dirección")
    email=models.EmailField(unique=True)
    imagen=models.ImageField(null=True, blank=True, upload_to='Emprendedores')
    tfno=models.CharField(max_length=10, verbose_name="teléfono")
    facebook=models.CharField(max_length=100, null=True, blank=True)
    twitter=models.CharField(max_length=100, null=True, blank=True)
    instagram=models.CharField(max_length=100, null=True, blank=True)
    whatsapp=models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return '{}'.format(self.email)
        # return "Emprendedor con cédula %d y apellido %s" % (self.cedula, self.apellidos)

    class Meta:
        verbose_name_plural= "Emprendedores"
        ordering=['nombres', "apellidos"]

class Categoria(models.Model):
    nombre= models.CharField(max_length=50, help_text='Nombre de Categoría', unique=True)
    descripcion=models.TextField(max_length=100, null=True, blank=True)
    imagen=models.ImageField(null=True, blank=True, upload_to="Categorias")

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural='Categorías'
        ordering=['nombre']

class Emprendimiento(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=500, help_text='Descripción del Emprendimiento', verbose_name="descripción", null=True, blank=True)
    direccion=models.CharField(max_length=150, help_text='Dirección del emprendimiento', verbose_name='dirección')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion=models.DateField(verbose_name='fecha de creación')
    imagen=models.ImageField(null=False, blank=False, upload_to='Emprendimientos')
    emprendedores=models.ManyToManyField(Emprendedor)

    def __str__(self):
        return '{}'.format(self.nombre)

    # def save(self):
    #     self.descripcion = self.descripcion.upper()
    #     super(Emprendimiento, self).save()

    class Meta:
        ordering=['nombre']
        verbose_name_plural= "Emprendimientos"

class Producto(models.Model):
    codigo=models.CharField(max_length=20, verbose_name="código", unique=True)
    nombre=models.CharField(max_length=30)
    marca=models.CharField(max_length=20)
    descripcion=models.TextField(max_length=500, help_text='Descripción del Producto', verbose_name="descripción", null=True, blank=True)
    precio=models.FloatField(default=0)
    emprendimiento= models.ForeignKey(Emprendimiento, on_delete=models.CASCADE)
    imagen=models.ImageField(null=False, blank=False, upload_to='Productos')

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural="Productos"
        ordering=['nombre']

class Contacto(models.Model):
    asunto=models.CharField(max_length=120)
    nombre=models.CharField(max_length=30)
    email=models.EmailField()
    telefono=models.CharField(max_length=10, verbose_name="teléfono")
    mensaje=models.TextField()

    def __str__(self):
        return '{}'.format(self.nombre)

