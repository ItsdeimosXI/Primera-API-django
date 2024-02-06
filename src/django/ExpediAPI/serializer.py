from rest_framework import serializers
from .models import expedientes, Proveedor

class expedientesSerializer(serializers.ModelSerializer):
        class Meta:
            model=expedientes
            fields = '__all__'

class provedorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proveedor
        fields= '__all__'