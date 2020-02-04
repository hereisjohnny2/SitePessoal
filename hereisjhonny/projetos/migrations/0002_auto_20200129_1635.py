# Generated by Django 3.0.2 on 2020-01-29 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_article',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Artigo do Projeto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_colaborators',
            field=models.TextField(blank=True, null=True, verbose_name='Colaboradores do Projeto'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_repository',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Repositório do Projeto no Github'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_site',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Site do Projeto'),
        ),
    ]