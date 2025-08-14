from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.filter(is_active=True)
    serializer_class = serializers.PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = models.PostComment.objects.all()
    serializer_class = serializers.CommentSerializer


class TagViewSet(ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
