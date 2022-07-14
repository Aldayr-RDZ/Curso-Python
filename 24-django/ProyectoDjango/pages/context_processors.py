from pages.models import Page



# Creamos un context proccesor que nos va a permitir ver las paginas que "cree" en la base de datos 

def get_pages(request):

    #no usamos .all ya que nos sacara un objeto de pagina y es mucho recurso
    pages = Page.objects.filter(visible=True).order_by("order").values_list('id','title', 'slug') # values_list es como un select 
    #flat = true es igual a texto plano
    return {
        'pages': pages
    }