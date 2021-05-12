from django.db import models


class Locations(models.Model):
    note = models.TextField(blank=True, verbose_name='Примечание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_deleted = models.DateTimeField(auto_now=True, verbose_name='Дата удаления')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    production_id = models.ForeignKey('Productions', on_delete=models.PROTECT, null=True)
    workshop_id = models.ForeignKey('Workshops', on_delete=models.PROTECT, null=True)
    compartment_id = models.ForeignKey('Compartments', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Местоположение оборудования'
        verbose_name_plural = 'Местоположения оборудований'



class Workshops(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    note = models.TextField(blank=True, verbose_name='Примечание')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_deleted = models.DateTimeField(auto_now=True, verbose_name='Дата удаления')
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'
        ordering = ['name']


class Compartments(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'
        ordering = ['name']


class Productions(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производство'
        verbose_name_plural = 'Производства'
        ordering = ['name']


class Controller_families(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_deleted = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Семейство контроллера'
        verbose_name_plural = 'Семейство контроллеров'
        ordering = ['name']
