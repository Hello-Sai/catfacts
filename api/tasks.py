from celery import shared_task
import requests
from django.core.cache import cache
@shared_task
def queue_data():
    cache.set('is_data_queued',True)
    response = requests.get('https://cat-fact.herokuapp.com/facts')

    cache.set('get-fact', response.json(),timeout=60)
    return
