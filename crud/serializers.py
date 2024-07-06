from rest_framework import serializers
from .models import ProductoModel


class ProductoSerializer(serializers.ModelSerializer):
    def validate_precio(self, precio):
        if precio < 0:
            raise serializers.ValidationError(
                "El precio debe ser mayor a cero")
        return precio

    def validate_nombre(self, nombre):
        if len(nombre) <= 5:
            raise serializers.ValidationError(
                "Tu texto tiene muy pocos caracteres")
        return nombre

    class Meta:
        model = ProductoModel
        fields = '__all__'

        def get_photo_url(self, obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_uri(photo_url)
