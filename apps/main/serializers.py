from rest_framework.serializers import ModelSerializer

from . import models


class PostSerializer(ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    owner = UserSerializer(many=False)

    class Meta:
        model = models.PostComment
        fields = '__all__'
