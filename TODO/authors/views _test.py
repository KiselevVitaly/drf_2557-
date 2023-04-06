from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serialiazers import AuthorModelSerializer
from rest_framework.views import APIView


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    
class ArticleAPIVIew(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)