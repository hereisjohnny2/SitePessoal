from django.db import models

class Colaborator(models.Model):
    colaborator_name = models.CharField("Coladorador", max_length=200)
    colaborator_repository = models.CharField("Repositório", max_length=200, blank=True, null=True)

    def __str__(self):
        return self.colaborator_name

class PrintImage(models.Model):
    image_legend = models.CharField("Legenda da Imagem", max_length=200)
    image_url = models.ImageField("Selecione uma imagem")
    image_description = models.TextField("Descrição da Imagem")

    def __str__(self):
        return self.image_legend

class Project(models.Model):
    project_name = models.CharField("Nome do Projeto", max_length=200)
    project_start_date = models.DateField("Data de Início")
    project_end_date = models.DateField("Data de Término")
    project_short_description = models.CharField("Descrição Breve do Projeto", max_length=200, default="")
    project_description = models.TextField("Descrição do Projeto")
    project_tecnologies = models.CharField("Tecnologias Utilizadas", max_length=500)
    project_repository = models.CharField("Repositório do Projeto no Github", max_length=500, blank=True, null=True)
    project_site = models.CharField("Site do Projeto", max_length=500, blank=True, null=True)
    project_article = models.CharField("Artigo do Projeto", max_length=500, blank=True, null=True)
    project_colaborators = models.ManyToManyField(Colaborator, help_text="Colaboradores do Projeto", blank=True, null=True)
    project_images = models.ManyToManyField(PrintImage, help_text="Imagens do Projeto", blank=True, null=True)

    def __str__(self):
        return self.project_name

    