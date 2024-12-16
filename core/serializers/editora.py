from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

    def validate_email(self, email):
        return email.lower()
