from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rss.api.serializers import NewsSerializer
from rss.models import NEWS


class NewsPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 1000



class NewsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = NEWS.objects.all().order_by('-id')
    serializer_class = NewsSerializer
    pagination_class = NewsPagination