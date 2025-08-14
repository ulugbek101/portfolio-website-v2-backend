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


class TagSerializer(ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    owner = UserSerializer(many=False)
    tag = TagSerializer(many=True)

    class Meta:
        model = models.PostComment
        fields = '__all__'
