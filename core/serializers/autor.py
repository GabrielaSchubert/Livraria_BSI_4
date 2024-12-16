from rest_framework.serializers import ModelSerializer

from core.models import Autor, Categoria, Editora


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
