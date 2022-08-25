from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from core_apps.articles.models import Article
from .models import Comments
from .serializers import CommentSerializer


class CommentAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def post(self, request, **kwargs):
        try:
            slug = self.kwargs.get("slug")
            article = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise NotFound("That article does not exists")

        comment = request.data
        author = request.user
        comment["author"] = author.pkid
        comment["article"] = article.pkid

        serializer = self.get_serializer(data=comment)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, **kwargs):
        try:
            slug = self.kwargs.get("slug")
            article = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise NotFound("That article does not exists")

        try:
            comments = Comments.objects.filter(article_id=article.pkid)
        except Comments.DoesNotExist:
            raise NotFound("Comment not found")

        serializer = CommentSerializer(comments, many=True, context={"request": request})
        return Response({
            "num_comments": len(serializer.data),
            "comments": serializer.data,
        }, status=status.HTTP_200_OK)


class CommentUpdateDeleteAPIVIew(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def put(self, request, slug, id):
        try:
            comment_to_update = Comments.objects.get(id=id)
        except Comments.DoesNotExist:
            raise NotFound("Comment not found")

        data = request.data
        serializer = self.get_serializer(comment_to_update, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Comment update successfully",
            "comment": serializer.data
        }, status=status.HTTP_200_OK)

    def delete(self, request, slug, id):
        try:
            comment_to_delete = Comments.objects.get(id=id)
        except Comments.DoesNotExist:
            raise NotFound("Comment not found")

        comment_to_delete.delete()
        return Response({
            "message": "Comment deleted successfully",
        }, status=status.HTTP_200_OK)


