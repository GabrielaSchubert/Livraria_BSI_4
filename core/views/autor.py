from rest_framework.viewsets import ModelViewSet

from core.models import Categoria, Editora, Autor
from core.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer