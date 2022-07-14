from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at') #Agregar created_at y update_at en visualizacion de articulos (admin)



# Agregar mis tablas a mi panel de gestion en django (admin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el titulo del panel 
title= "Máster en Python - Aldayr Rodriguez"
admin.site.site_header=title
admin.site.site_title =title
admin.site.index_title = "Panel de gestión"
