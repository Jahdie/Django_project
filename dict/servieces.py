from dict.models import *
import openpyxl


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


# def uploadControllerFamilies():
#     ControllerFamilies.objects.create(name_controller_families='90-30', note_controller_families='!!!!')
#     ControllerFamilies.objects.create(name_controller_families='RX7', note_controller_families='!!!!')
#     ControllerFamilies.objects.create(name_controller_families='Genius', note_controller_families='!!!!')
#     ControllerFamilies.objects.create(name_controller_families='90-70', note_controller_families='!!!!')
#
#
# def uploadStations():
#     Stations.objects.create(name_stations='AC8', note_stations='!!!!')
#     Stations.objects.create(name_stations='REAG', note_stations='!!!!')
#     Stations.objects.create(name_stations='NU-1', note_stations='!!!!')
#     Stations.objects.create(name_stations='AC7', note_stations='!!!!')


# TODO зарефакторить логику выбора словаря
# def getModelByNumber(dict_number):
#     if dict_number == 1:
#         _dict = Productions.objects.values_list()
#     elif dict_number == 2:
#         _dict = Workshops.objects.values_list()
#     elif dict_number == 3:
#         _dict = Compartments.objects.values_list()
#     return _dict
def getModelByNumber(request, dict_number):
    id_from_request = request.GET
    hierarchy = 1
    if dict_number == hierarchy:
        model_content = Productions.objects.filter(id_from_request)
        model_content_list = []
        # model_content = model_content.append(('2',))
        for item in model_content:
            hierarchy_tuple = (dict_number - 1, dict_number, dict_number + 1)
            item_hierarchy_tuple = (item, hierarchy_tuple)
            model_content_list.append(item_hierarchy_tuple)
        # TODO продумать алгоритм добавления иерархии


    elif dict_number == hierarchy + 1:
        id_from_request = request.GET
        if id_from_request:
            model_locations_locations = Locations.objects.filter(workshop_id_id=int(id_from_request['ID']))
            for item in model_locations_locations:
                my_a = item.compartment_id
        # model_content = Workshops.objects.filter()
        # model_content_list = []
        # # model_content = model_content.append(('2',))
        # for item in model_content:
        #     hierarchy_tuple = (dict_number - 1, dict_number, dict_number + 1)
        #     item_hierarchy_tuple = (item, hierarchy_tuple)
        #     model_content_list.append(item_hierarchy_tuple)
        # # TODO продумать алгоритм добавления иерархии
    elif dict_number == hierarchy + 2:
        id_from_request = request.GET
        model_content = Compartments.objects.values_list()
        model_content_list = []
        # model_content = model_content.append(('2',))
        for item in model_content:
            hierarchy_tuple = (dict_number - 1, dict_number, dict_number + 1)
            item_hierarchy_tuple = (item, hierarchy_tuple)
            model_content_list.append(item_hierarchy_tuple)
    return model_content_list


def getModelByNumberNumber(related_dict_number):
    if related_dict_number == 1:
        _dict = Productions.objects.values_list()
    elif related_dict_number == 2:
        _dict = Workshops.objects.values_list()
    elif related_dict_number == 3:
        _dict = Compartments.objects.values_list()
    return _dict


def getContentFromFile():
    table_location = 'C:\\Users\\Admin\\PycharmProjects\\Django_project\\media\\dicts\\1.xlsx'
    work_book = openpyxl.load_workbook(table_location, read_only=True)
    first_sheet = work_book.worksheets
    for row in first_sheet[0].rows:
        model = Productions.objects.create(
            name= row[0].value
        )
    print(first_sheet)
# Dict.objects.create(title='',...)
# Dict.Objects.all()
# Dict.Objects.filter(title='')
# Dict.Objects.get(pk=5)
# dict.name = '...'
# dict.save()
# dict.delete()
# Dict.Objects.order_by().all()
# Dict.Objects.exclude(name ='')
