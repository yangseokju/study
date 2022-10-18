from rest_framework import serializers
from .models import Music, Comment


class MusicListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ("id", "title")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ('music',)


class MusicSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Music
        fields = "__all__"