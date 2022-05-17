from celery import shared_task
from rss.models import RSS, NEWS
from datetime import datetime

@shared_task
def insert_news():
    last_news = NEWS.objects.last()
    if last_news:
        last_rss = last_news.rss.all()[-1]
        rsses = RSS.objects.filter(time__lt=last_rss.time)
        new_news = NEWS.objects.create()
        new_news.rss.add(*rsses)
    else:
        rsses = RSS.objects.filter(time__lt=datetime.now())
        new_news = NEWS.objects.create()
        new_news.rss.add(*rsses)
    