from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    def get(self,request):
        return Response({'status_code' : 200},status=200)
    
class FetchFactView(APIView):
    def get(self,request):
        from api.tasks import queue_data

        queue_data.delay()
        if cache.get('is_data_queued'):
            return Response({"success":True})

        return Response({'error':'TaskQueue is not running please check once.'},status=400)
    

class GetFactView(APIView):
    def get(self,request):
        if cache.get('get-fact'):
            return Response(cache.get('get-fact'))
        cache.get_backend_timeout()
        return Response({'error':'notask_has_been_queued_yet'},status=400)