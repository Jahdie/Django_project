from django.shortcuts import render
from django.http import HttpResponse
from dict.servieces import *
from django.shortcuts import render


# Create your views here.
def index(request):
    # print(dir(request))
    uploadWorkshops()
    uploadCompartments()
    uploadControllerFamilies()
    uploadProductions()
    uploadStations()
    # dict_compartments = Compartments.objects.all()
    # return render(request, 'dict/index.html', {'dicts': dict_workshops, 'title': 'Список'})
    return render(request, 'dict/index.html', {'title': 'список словарей'})


def getListDictionary(request, dict_number):
    _dict = getModelByNumber(dict_number)
    res = render(request, './dict/dicts.html', {'dicts': _dict, 'title': 'список цехов'})
    return res

def getListRelatedDictionary(request, dict_number, dict_number_number):
    _dict = getModelByNumberNumber(dict_number_number)
    res = render(request, './dict/related_dicts.html', {'dicts_related': _dict, 'title': 'список цехов'})
    return res
# def getListDictionaryControllerFamilies(request):
#     _dict = Controller_families.objects.all()
#     res = render(request, './dict/dicts.html', {'dicts': _dict, 'title': 'список цехов'})
#     return res
#
# def getListDictionaryProductions(request, dict_number):
#     _dict = getModelByNumber(dict_number)
#     res = render(request, './dict/dicts.html', {'dicts': _dict, 'title': 'список цехов'})
#     return res
#
# def getListDictionaryLocations(request):
#     _dict =Productions.objects.all()
#     res = render(request, './dict/dicts.html', {'dicts': _dict, 'title': 'список цехов'})
#     return res

def upload(request):
    print(dir(request))
    return HttpResponse('!!')
