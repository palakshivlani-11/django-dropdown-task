from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Country,State,District,City)
class ViewAdmin(ImportExportModelAdmin):
    pass


admin.site.register(UserResponses)