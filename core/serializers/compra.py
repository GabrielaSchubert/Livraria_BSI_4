from rest_framework.serializers import ModelSerializer, CharField

from core.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"
    
        usuario = CharField(source="usuario.email", read_only=True) # inclua essa linha
        status = CharField(source="get_status_display", read_only=True) # inclua essa linha
