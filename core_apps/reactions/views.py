from rest_framework import permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

from core_apps.articles.models import Article
from .models import Reaction
from .serializers import ReactionSerializer


def find_article_helper(slug):
    try:
        Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise NotFound(f"Article with the slug: {slug} does not exist.")


class ReactionAPIVIew(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReactionSerializer

    def set_reaction(self, article, user, reaction):
        try:
            existin_recation = Reaction.object.get(article=article)
            existin_recation.delete()

            data = {
                "article": article.pkid,
                "user": user.pkid,
                "reaction":reaction
            }
            serializer = self.serializer_class(data=data)
            serializer.is_valid(raise_exception=True)

            response = {"message": "Reaction added"}
            status_code = status.HTTP_201_CREATED
            return response, status_code
        except Reaction.DoesNotExist:
            raise NotFound
