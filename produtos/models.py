from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=20,default='')
    preco = models.IntegerField(default=0,)



    def __str__(self):
        return self.nome + ' --- ' + str(self.preco)
