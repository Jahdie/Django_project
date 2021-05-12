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


def uploadProductions():
    Productions.objects.create(name='НОФ', note='!!!!')
    Productions.objects.create(name='УФМК', note='!!!!')
    Productions.objects.create(name='ЦГТС', note='!!!!')
    Productions.objects.create(name='Лебяжье', note='!!!!')


def uploadController_families():
    Controller_families.objects.create(name='90-30', note='!!!!')
    Controller_families.objects.create(name='RX7', note='!!!!')
    Controller_families.objects.create(name='Genius', note='!!!!')
    Controller_families.objects.create(name='90-70', note='!!!!')


def getModelByNumber(dict_number):
    if dict_number == 1:
        _dict = Workshops.objects.all()
    elif dict_number == 2:
        _dict = Productions.objects.all()
    return _dict

    # Dict.objects.create(title='',...)
# Dict.Objects.all()
# Dict.Objects.filter(title='')
# Dict.Objects.get(pk=5)
# dict.name = '...'
# dict.save()
# dict.delete()
# Dict.Objects.order_by().all()
# Dict.Objects.exclude(name ='')
