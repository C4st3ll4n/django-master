from drf_haystack.serializers import HaystackSerializer

from .search_index import ArticleIndex


class ArticleSearchSerializer(HaystackSerializer):
    class Meta:
        index_classes = [ArticleIndex]
        fields = ["author", "title", "body", "autocomplete, created_at", "updated_at"]

        ignore_fields = ["autocomplete"]
        fields_aliases = {"q": "autocomplete"}
