from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .exceptions import CantRateYourArticle, AlreadyRated
from .models import Rating
from ..articles.models import Article


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_article_rating_view(request, article_id):
    author = request.user
    article = Article.objects.get(id=article_id)
    data = request.data

    if article.author == author:
        raise CantRateYourArticle

    already_rated = article.article_ratings.filter(rated_by_pkid=author.pkid)
    if already_rated:
        raise AlreadyRated
    elif data['value'] == 0:
        formatted_response = {
            "detail": "You can't give a zero rate"
        }
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
    else:
        rating = Rating.objects.create(article=article, rated_by=author, value=data["value"], review=data["review"])
        return Response({
            "success": "Rating has been added"
        }, status=status.HTTP_201_CREATED)
