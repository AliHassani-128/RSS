from rest_framework import serializers
from rss.models import RSS, NEWS


class RssSerializer(serializers.ModelSerializer):

    class meta:
        model = RSS

class NewsSerializer(serializers.ModelSerializer):

    class meta:
        model = NEWS
