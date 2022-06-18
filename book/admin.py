from django.contrib import admin
from . models import Author,Book
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'last_name', 'nationality']
    list_display = ['id', 'name', 'last_name', 'nationality']
    resource_class = AuthorResource

############################################################################

class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title', 'publication_date']
    list_display = ['title', 'publication_date', 'author_id']
    resource_class = BookResource    

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
