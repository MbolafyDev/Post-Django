from django.contrib import admin

from . models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date') # Affiche un tableau de filtrage sur le template admin
    list_display = ('date', 'title', 'author') # Affiche dans le tableau le vrai nom du champs
    prepopulated_fields = {"slug": ("title",)} # Auto complete Slug

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
