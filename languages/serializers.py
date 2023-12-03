from rest_framework.serializers import ModelSerializer, Serializer, SerializerMethodField

from .models import Laptop, PCs


class LaptopsSerializer(ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'


class PCSerializer(ModelSerializer):
    class Meta:
        model = PCs
        fields = '__all__'


class LaptopPCsSerializer(Serializer):
    category = LaptopsSerializer(many=True)
    PCs = PCSerializer(many=True)