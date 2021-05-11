from dict.models import *


def uploadWorkshops():

    Workshops.objects.create(name='ДЦ', note='!!!!')
    Workshops.objects.create(name='ИФЦ', note='!!!!')
    Workshops.objects.create(name='КД', note='!!!!')
    Workshops.objects.create(name='Курьер', note='!!!!')


def uploadCompartments():
    Compartments.objects.create(name='ПСУ_1F', note='!!!!')
    Compartments.objects.create(name='ОФ_1сек', note='!!!!')
    Compartments.objects.create(name='Комплекс_Nelson4', note='!!!!')
    Compartments.objects.create(name='Комплекс_Nelson2', note='!!!!')


# Dict.objects.create(title='',...)
# Dict.Objects.all()
# Dict.Objects.filter(title='')
# Dict.Objects.get(pk=5)
# dict.name = '...'
# dict.save()
# dict.delete()
# Dict.Objects.order_by().all()
# Dict.Objects.exclude(name ='')

