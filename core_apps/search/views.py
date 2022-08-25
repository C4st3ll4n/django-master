from drf_haystack.filters import HaystackAutocompleteFilter
from drf_haystack.viewsets import HaystackViewSet
from rest_framework import permissions

from core_apps.articles.models import Article
from core_apps.search.serializers import ArticleSearchSerializer


class SearchArticleView(HaystackViewSet):
    permission_classes = [permissions.AllowAny]
    index_models = [Article]
    serializer_class = ArticleSearchSerializer
    filter_backends = [HaystackAutocompleteFilter]
