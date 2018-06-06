from django.contrib import admin
from .models import Produtos






class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['nome']


admin.site.register(Produtos, ProdutoAdmin)
