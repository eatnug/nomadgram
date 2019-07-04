from rest_framework import serializers
from . import models
from nomadgram.images import serializers as image_serializer

class ExploreUserSerializer(serializers.ModelSerializer):

    followings = image_serializer.FeedUserSerializer(many=True)
    followers = image_serializer.FeedUserSerializer(many=True)

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
            'followings',
            'followers'
        )