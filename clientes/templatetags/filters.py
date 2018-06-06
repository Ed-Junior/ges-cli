from django import template

register = template.Library()


@register.filter
def vazio(texto):
    return 'Não temos um nenhum cliente cadastrado'



