from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime.models import CrimeCctvModel


@api_view(['GET'])
@parser_classes([JSONParser])
def create_crime_model(request):
    CrimeCctvModel().create_crime_model()
    return JsonResponse({'connection': 'create_crime_model'})

def create_police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'connection': 'create_police_position'})