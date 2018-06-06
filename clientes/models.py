from django.db import models
from produtos.models import Produtos



class Documento(models.Model):
    num_doc = models.CharField(max_length=50, default='')
    ativo = models.BooleanField(default=False)


    @property
    def verf(self,):
        try:
            self.person
            return True
        except:
            return False

    def __str__(self):
        return self.num_doc




class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField(blank=True)
    produtos = models.ManyToManyField(Produtos, blank=True,)
    img = models.ImageField(upload_to='user_photo', null=True, blank=True)
    doc = models.OneToOneField(Documento, blank=False,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name



