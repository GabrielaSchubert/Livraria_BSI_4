from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Livro
from core.serializers import CategoriaSerializer
from core.serializers import LivroDetailSerializer, LivroSerializer, LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer