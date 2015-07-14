from django.contrib import admin
from .models import Palestrante, Apoiador


class PalestranteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class ApoiadorAdmin(admin.ModelAdmin):
    list_display = ('nome',)


admin.site.register(Palestrante, PalestranteAdmin)
admin.site.register(Apoiador, ApoiadorAdmin)
