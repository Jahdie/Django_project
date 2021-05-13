from dict.models import *


def uploadWorkshops():
    Workshops.objects.create(name_workshops='ДЦ', note_workshops='!!!!')
    Workshops.objects.create(name_workshops='ИФЦ', note_workshops='!!!!')
    Workshops.objects.create(name_workshops='КД', note_workshops='!!!!')
    Workshops.objects.create(name_workshops='Курьер', note_workshops='!!!!')


def uploadCompartments():
    Compartments.objects.create(name_compartments='ПСУ_1F', note_compartments='!!!!')
    Compartments.objects.create(name_compartments='ОФ_1сек', note_compartments='!!!!')
    Compartments.objects.create(name_compartments='Комплекс_Nelson4', note_compartments='!!!!')
    Compartments.objects.create(name_compartments='Комплекс_Nelson2', note_compartments='!!!!')


def uploadProductions():
    Productions.objects.create(name_productions='НОФ', note_productions='!!!!')
    Productions.objects.create(name_productions='УФМК', note_productions='!!!!')
    Productions.objects.create(name_productions='ЦГТС', note_productions='!!!!')
    Productions.objects.create(name_productions='Лебяжье', note_productions='!!!!')


def uploadController_families():
    ControllerFamilies.objects.create(name_controller_families='90-30', note_controller_families='!!!!')
    ControllerFamilies.objects.create(name_controller_families='RX7', note_controller_families='!!!!')
    ControllerFamilies.objects.create(name_controller_families='Genius', note_controller_families='!!!!')
    ControllerFamilies.objects.create(name_controller_families='90-70', note_controller_families='!!!!')


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
