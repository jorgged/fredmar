from django.contrib import admin
from .models import horarioEmpresa,misionEmpresa,visionEmpresa,telefonoEmpresa
# Register your models here.
class visionEmpresaAdmin(admin.ModelAdmin):
    list_display = ('vision',)
    search_fields = ['vision',]
    list_per_page = 20
admin.site.register(visionEmpresa, visionEmpresaAdmin)

class misionEmpresaAdmin(admin.ModelAdmin):
    list_display = ('mision',)
    search_fields = ['mision',]
    list_per_page = 20
admin.site.register(misionEmpresa, misionEmpresaAdmin)

class horarioEmpresaAdmin(admin.ModelAdmin):
    list_display = ('turno',)
    search_fields = ['turno',]
    list_per_page = 20
admin.site.register(horarioEmpresa, horarioEmpresaAdmin)

class telefonoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('tlf',)
    search_fields = ['tlf',]
    list_per_page = 20
admin.site.register(telefonoEmpresa, telefonoEmpresaAdmin)