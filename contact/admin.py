from django.contrib import admin
from . models import Contact
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class ContactAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['name', 'last_name', 'email']
    list_display = ['name', 'last_name',  'email']
    resource_class = ContactResource


admin.site.register(Contact,ContactAdmin)