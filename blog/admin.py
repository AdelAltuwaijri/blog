from django.contrib import admin
from .models import Post,Comment,Myresume
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Myresume)
@admin.register(Post)
class PostImportExport(ImportExportModelAdmin):
    pass

admin.site.register(Comment)