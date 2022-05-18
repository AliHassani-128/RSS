from rest_framework import serializers
from rss.models import RSS, NEWS


class RssSerializer(serializers.ModelSerializer):

    class Meta:
        model = RSS
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = NEWS
        fields = '__all__'
