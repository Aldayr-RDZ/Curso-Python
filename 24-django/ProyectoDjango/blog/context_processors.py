from blog.models import Category, Article


# Creamos un context proccesor que nos va a permitir ver las paginas que "cree" en la base de datos 

def get_categories(request):

    #no usamos .all ya que nos sacara un objeto de pagina y es mucho recurso

    categories_in_use= Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id','name') # values_list es como un select 
    #flat = true es igual a texto plano
    return {
        'categories': categories,
        'ids':categories_in_use
    }