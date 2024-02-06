from .models import Proveedor, expedientes
from rest_framework import viewsets, permissions
from .serializer import provedorSerializer, expedientesSerializer
class ProveedorViewset(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = provedorSerializer

class ExpedienteViewset(viewsets.ModelViewSet):
    queryset = expedientes.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = expedientesSerializer
   