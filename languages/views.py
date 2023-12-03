from collections import namedtuple

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import LaptopPCsSerializer
from .models import Laptop , PCs

PCsAndLaptop = namedtuple('PCsAndLaptop', ('laptop', 'PCs'))


# Create your views here.
class LaptopsAndPCsListAPIView(ListAPIView):
    serializer_class = LaptopPCsSerializer

    def list(self, request, *args, **kwargs):
        try:
            lang = request.GET['lang']
        except:
            lang = 'uz'

        all_laptop =Laptop.objects.all()
        all_PCs = PCs.objects.all()

        PCs_and_laptop = PCsAndLaptop(
            laptop = all_laptop,
            PCs = all_PCs
        )
        serializer = LaptopPCsSerializer(PCs_and_laptop)
        return Response(serializer.data)