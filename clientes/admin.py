from django.contrib import admin

from .models import Person, Documento


class PersonAdmin(admin.ModelAdmin):
    # Exibe somente os fields listados
    # cuidado para não esquecer os obrigatorios
    #fields = (('first_name','last_name'),('salary','doc', 'age'),'img','bio',)
    # fields a não ser listados
    # exclude = ('bio')

    # configuraçoes dos fields
    fieldsets = (
        ('Dados Pessoais',{'fields':('first_name','last_name','doc','produtos')}),
        ('Dados Complementares',
         {
             'classes': ('collapse',),
             'fields':(('salary','age'),'img','bio')

          }
         ),

    )

    filter_horizontal = ['produtos']
    autocomplete_fields = ['produtos']



    #configuraçoes do display
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).upper()

    upper_case_name.short_description = 'Name'

    list_display = ('upper_case_name', 'first_name','last_name', 'age','doc','img')
    list_display_links = ('first_name', 'last_name','upper_case_name') # None pede ser passado
    actions_on_top = True
    list_filter = ('age', 'first_name')

    search_fields = ['first_name']








admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)





