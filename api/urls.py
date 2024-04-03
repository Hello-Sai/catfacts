from django.urls import path
from api.views import *

urlpatterns = [
    path('health_check',HealthCheckView.as_view()),
    path('fetch_fact',FetchFactView.as_view()),
    path('get_fact',GetFactView.as_view()),
]