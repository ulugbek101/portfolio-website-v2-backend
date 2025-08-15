from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from . import models


class TagSerializer(ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class PostSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = PrimaryKeyRelatedField(
        many=True, queryset=models.Tag.objects.all(), write_only=True
    )

    class Meta:
        model = models.Post
        fields = '__all__'

    def create(self, validated_data):
        tag_ids = validated_data.pop('tag_ids', [])
        post = super().create(validated_data)
        post.tags.set(tag_ids)
        return post

    def update(self, instance, validated_data):
        tag_ids = validated_data.pop('tag_ids', None)
        post = super().update(instance, validated_data)
        if tag_ids is not None:
            post.tags.set(tag_ids)
        return post


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    owner = UserSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = models.PostComment
        fields = '__all__'
