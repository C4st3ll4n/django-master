from rest_framework import serializers

from .custom_tag_field import TagRelatedField
from .models import ArticleViews, Article
from ..comments.serializers import CommentListSerializer
from ..ratings.serializers import RatingSerializer


class ArticleViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleViews
        exclude = ["updated_at", "pkid"]


class ArticleSerializer(serializers.ModelSerializer):
    author_info = serializers.SerializerMethodField(read_only=True)
    banner_image = serializers.SerializerMethodField()
    read_time = serializers.ReadOnlyField(source="article_read_time")
    ratings = serializers.SerializerMethodField()
    num_ratings = serializers.SerializerMethodField()
    average_rating = serializers.ReadOnlyField(source="get_average_rating")
    like = serializers.ReadOnlyField(source="article_reactions.like")
    dislike = serializers.ReadOnlyField(source="article_reactions.dislike")
    tagList = TagRelatedField(many=True, required=False, source="tags")
    comments = serializers.SerializerMethodField()
    num_comments = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_banner_image(self, obj):
        return obj.banner_image.url

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

    def get_author_info(self, obj):
        return {
            "username": obj.author.username,
            "fullname": obj.author.get_full_name,
            "about_me": obj.author.profile.about_me,
            "profile_photo": obj.author.profile.profile_photo.url,
            "twitter_handle": obj.author.twitter_handle,
            "email": obj.author.email,
        }

    def get_ratings(self,obj):
        reviews = obj.article_ratings.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data

    def get_num_ratings(self,obj):
        num_reviews = obj.article_ratings.all().count()
        return num_reviews

    def get_comments(self,obj):
        comments = obj.comments.all()
        serializer = CommentListSerializer(comments, many=True)
        return serializer.data

    def get_num_comments(self,obj):
        num_comments = obj.comments.all().count()
        return num_comments

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "slug",
            "tagList",
            "description",
            "body",
            "banner_image",
            "read_time",
            "author_info",
            "likes",
            "dislikes",
            "ratings",
            "num_ratings",
            "average_rating",
            "views",
            "num_comments",
            "comments",
            "created_at",
            "updated_at",
        ]


class ArticleCreateSerializer(serializers.ModelSerializer):
    tags = TagRelatedField(required=False, many=True)
    banner_image = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Article
        exclude = ["updated_at", "pkid"]


    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date


    def get_banner_image(self, obj):
        return obj.banner_image.url


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["title", "description", "tags", "body", "banner_image", "updated_at"]

    tags = TagRelatedField(required=False, many=True)
    banner_image = serializers.SerializerMethodField()
    updated = serializers.SerializerMethodField()

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date

