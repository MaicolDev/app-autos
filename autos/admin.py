from django.contrib import admin
from .models import Auto
# Register your models here.

class AutoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha',)

admin.site.register(Auto,AutoAdmin)