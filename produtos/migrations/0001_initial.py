# Generated by Django 2.0.3 on 2018-05-25 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=20)),
                ('preco', models.IntegerField(default=0)),
            ],
        ),
    ]