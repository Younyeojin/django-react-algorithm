from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crawling.models import Crawling


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    Crawling().process()
    return JsonResponse({'result': 'Create Crawling Success'})
@api_view(['GET'])
@parser_classes([JSONParser])
def samsung_report(request):
    Crawling().samsung_report()
    return JsonResponse({'result': 'samsung_report Success'})
@api_view(['GET'])
@parser_classes([JSONParser])
def naver_movie(request):
    Crawling().naver_movie()
    return JsonResponse({'result': 'naver_movie Success'})
@api_view(['GET'])
@parser_classes([JSONParser])
def tweet_trup(request):
    Crawling().tweet_trup()
    return JsonResponse({'result': 'tweet_trup Success'})