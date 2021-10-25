from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from admin.myNLP.models import MyImdb, NaverMovie


@api_view(['GET'])
@parser_classes([JSONParser])
def imdb_process(request):
    MyImdb().imdb_process()
    return JsonResponse({'imdb_process' : 'Success'})


@api_view(['GET'])
@parser_classes([JSONParser])
def web_scraping(request):
    NaverMovie().web_scraping()
    return JsonResponse({'web_scraping' : 'Success'})