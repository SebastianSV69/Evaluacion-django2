from django.contrib import admin
from veterinaria.models import Cliente, Atencion

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    list_display = ("nombre","correo","numero")
    list_filter = ("nombre","correo","numero")
    search_fields = ("nombre","correo","numero")


@admin.register(Atencion)
class AdminAtencion(admin.ModelAdmin):
    list_display = ("nombre","Cliente","horarioAtencion","precio")
    list_filter = ("Cliente","horarioAtencion","precio")
    search_fields = ("Cliente","horarioAtencion")

