from rest_framework import serializers

from .models import Comments


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    class Meta:
        model = Comments
        fields = ["id", "article", "author", "body", "created_at", "updated_at"]


class CommentListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.user.username")
    article = serializers.ReadOnlyField(source="article.tittle")

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    class Meta:
        model = Comments
        fields = ["id", "article", "author", "body", "created_at", "updated_at"]

