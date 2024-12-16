from rest_framework.viewsets import ModelViewSet

from core.models import Autor, Categoria, Editora
from core.serializers import AutorSerializer, CategoriaSerializer, EditoraSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
