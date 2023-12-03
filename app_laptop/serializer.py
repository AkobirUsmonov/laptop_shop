from rest_framework.serializers import ModelSerializer, SerializerMethodField, Serializer

from .models import PC,Laptop


class PCsSerializer(ModelSerializer):
    class Meta:
        model = PC
        fields = ['id','name', 'processor', 'memory', 'storage','price']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'processor': {'read_only': True}
        }


class LaptopSerializer(ModelSerializer):
    class Meta:
        model =Laptop
        fields = ['id', 'brand', 'model_name', 'price','processor','ram', 'storage','graphics_card','screen_size','weight','battery_life']
        extra_kwargs = {
            'id': {'read_only': True}
        }
