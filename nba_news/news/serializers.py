from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image_url', 'publish_date', 
            'source_url')
