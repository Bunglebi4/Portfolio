from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название проекта', blank=True)
    short_description = models.TextField(verbose_name='Краткое описание проекта', blank=True)
    full_description = models.TextField(verbose_name='Полное описание проекта', blank=True)
    image = models.ImageField(verbose_name='Обложка', blank=True)
    source = models.CharField(max_length=50, verbose_name='Ссылка на исходный код', blank=True)
    link = models.CharField(max_length=50, verbose_name='Ссылка на проект', blank=True)
    datetime = models.DateTimeField(verbose_name='Дата и время добавления в портфолио', blank=True)


    def __str__(self):
        return self.title