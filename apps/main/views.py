from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class PostViewSet(ModelViewSet):
    queryset = models.Post.objects.filter(is_active=True)
    serializer_class = serializers.PostSerializer

