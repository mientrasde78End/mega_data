from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "username",
            "created_at"
        ]