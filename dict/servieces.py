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


def uploadControllerFamilies():
    ControllerFamilies.objects.create(name_controller_families='90-30', note_controller_families='!!!!')
    ControllerFamilies.objects.create(name_controller_families='RX7', note_controller_families='!!!!')
    ControllerFamilies.objects.create(name_controller_families='Genius', note_controller_families='!!!!')
    ControllerFamilies.objects.create(name_controller_families='90-70', note_controller_families='!!!!')

def uploadStations():
    Stations.objects.create(name_stations='AC8', note_stations='!!!!')
    Stations.objects.create(name_stations='REAG', note_stations='!!!!')
    Stations.objects.create(name_stations='NU-1', note_stations='!!!!')
    Stations.objects.create(name_stations='AC7', note_stations='!!!!')


def getModelByNumber(dict_number):
    if dict_number == 1:
        _dict = Productions.objects.values_list()
    elif dict_number == 2:
        _dict = Workshops.objects.values_list()
    elif dict_number == 3:
        _dict = Compartments.objects.values_list()
    return _dict

def getModelByNumberNumber(dict_number_number):
    if dict_number_number == 1:
        _dict = ControllerFamilies.objects.values_list()
    elif dict_number_number == 2:
        _dict = Workshops.objects.values_list()
    elif dict_number_number == 3:
        _dict = Compartments.objects.values_list()
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
