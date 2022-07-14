

from django.http import HttpResponse
from django.shortcuts import redirect, render
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

# Create your views here.
#MCV = Modelo Vista Controlador -- Acciones  (metoodos)


#MVT = Modelo Template Vista -- Acciones (metodos)


layout = """
 <h1>Sitio web con Django | Aldayr Rdz </h1>
 <hr/>

 <ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo</a>
    </li>
    <li>
        <a href="/pagina-pruebas">Página de Pruebas</a>
    </li>
    <li>
        <a href="/contacto">Contacto</a>
    </li>
 </ul>
 <hr/>

"""

def index(request):
    
    # template ="""
    #     <h1>Inicio</h1>
    #     <p>Años hasta el 2050</p>
    #     <ul>
    # """
    # year = 2022
    # while year <=2050:
    #     if year %2 ==0:
    #         template += f"<li>{str(year)}</li>"
    #     year +=1
    # template += "</ul>"

    year = 2022
    hasta = range(year, 2050)


    nombre = "Aldayr Rodriguez"
    lenguajes = ['Javascript', 'Python', 'C']
    

    # return HttpResponse(layout + template)
    return render(request,'index.html', {
        'lenguajes':lenguajes,
        'nombre':nombre,
        'mi_variable':'soy un dato que esta en la vista', 
        'years':hasta
        })

def hola_mundo(request):
    return render(request, 'hola-mundo.html')

def pagina(request, redirigir=0):

    if redirigir == 1:
        return redirect('contacto', nombre="Aldayr", apellidos="Rodriguez" )



    return render(request, 'pagina.html',{
        'texto': 'Este es mi texto ',
        'lista': ['uno','dos','tes']
    })

def contacto(request, nombre="", apellidos=""):

    html =""
    if nombre and apellidos:
        html +=f"<p>El nombre completo es: {nombre} {apellidos}</p>"
        

    
    return HttpResponse(layout + f"""
    <h2>Contacto {nombre}  {apellidos}</h2>
    """+ html)

def crear_articulo(request, title, content, public):
    articulo = Article(
        title= title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")

def save_article(request):

    # if request.method=='GET':
    #     title= request.GET['title']
    #     content= request.GET['content']
    #     public=request.GET['public']
    if request.method=='POST':
        title= request.POST['title']
        content= request.POST['content']
        public=request.POST['public']

        articulo = Article(
            title= title,
            content=content,
            public=public
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")
    else:
        return HttpResponse("No se ha podido crear el articulo")

        


def create_article(request):
    return render(request, 'create_article.html')


def create_full_article(request):
    
    if request.method=='POST':
        formulario=FormArticle(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            title = data_form['title']
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
            title= title,
            content=content,
            public=public
            )
            articulo.save()

            #Crear mensaje flash (Sesion que solo se muestra 1 vez)
            messages.success(request, f'Has creado correctamente el articulo {articulo.id}')

            return redirect('articulos')
        else:
            return render(request, 'create_full_article.html', {
             'form': formulario
            })
            # return HttpResponse(articulo.title + '-'+ articulo.content + '-' + articulo.public)
    else:
        # print("gpal")
        formulario=FormArticle()
        
    
    return render(request, 'create_full_article.html', {
        'form': formulario
    })


def articulo(request):
    try:
        articulo = Article.objects.get(id=1)
        response = f'Articulo: id : {articulo.id} - Titulo : {articulo.title}'
    except:
        response= "<h1>No se ha encontrado el articulo</h1>"
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo= Article.objects.get(pk=id)
    articulo.title = "Batman"
    articulo.content = "Pelicula del 2022"
    articulo.public = True
    articulo.save()

    return HttpResponse(f'Articulo {articulo.id} editado : {articulo.title}')

def articulos(request):
    # order_by("-id") desc 
    # order_by("-id")[:3] desc and limit
    # order_by("-id")[3:7] desc and limit del 3 al 7 
    #[0:1] limit 1
    # title__contains like en sql 
    # lookups investigar
    #gt id>3
    #gte id>=3
    #lte <=3
    #articulos= Article.objects.filter(id__gte=3, title__contains="Articulo") la coma significa AND
    articulos= Article.objects.filter(public=True).order_by('-id')

    # articulos= Article.objects.filter(id__gte=3)

    # articulos = Article.objects.filter(title="Articulo").exclude(public=False)

    # #Conuslta cruda de slq 
    # articulos= Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=0")

    # articulos= Article.objects.filter(Q(title__contains="2") | Q(title__contains="3"))

    return render(request, 'articulos.html', {
        'articulos':articulos
    })

def borrar_articulo(request, id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')
