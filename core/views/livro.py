from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Livro
from core.serializers import CategoriaSerializer, LivroSerializer

...
class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer