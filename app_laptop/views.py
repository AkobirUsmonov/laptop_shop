from collections import namedtuple

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.views import checkUserToken
from .filter import PCsLaptopFilterBackend

from .models import PC, Laptop
from .serializer import PCsSerializer, LaptopSerializer

PC_with_laptop = namedtuple('PC_with_laptop', ('PC', 'laptop'))


# Create your views here.
class LaptopCreateAPIView(CreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


class PCCreateAPIView(CreateAPIView):
    queryset = PC.objects.all()
    serializer_class = PCsSerializer


class PCsListAPIView(ListAPIView):
    queryset = PC.objects.all()
    serializer_class = PCsSerializer

    def get_queryset(self):
        user = self.kwargs['user']
        try:
            queryset = PC.objects.filter(title=user, is_active=True)
        except:
            queryset = PC.objects.none()
        return queryset


class DeleteAPIView(UpdateAPIView):
    serializer_class = None

    def update(self, request, *args, **kwargs):
        try:
            token = request.META['HTTP_TOKEN']
        except:
            raise AuthenticationFailed('Iltimos, avval tizimga kiring')

        user = checkUserToken(token)
        if not user:
            raise AuthenticationFailed('Iltimos, avval tizimga kiring')

        try:
            book_id = kwargs['book_id']
            queryset = PC.objects.filter(pk=book_id, title=request.user.id).update(
                is_active=False)
            return Response({'detail': 'Deleted'})
        except:
            return Response({'detail': 'Unexpected error'})


class PClaptopListAPIView(ListAPIView):
    filter_backends = (PCsLaptopFilterBackend,)

    def list(self, request, *args, **kwargs):
        try:
            title_1 = request.GET['title_1']

            PC_queryset = PC.objects.filter(title=title_1, is_active=True)

            Laptop_queryset = Laptop.objects.filter(
                laptop_point=PC_queryset[0].id, puplication_date=True)

            PC_with_laptop = PC_with_laptop(
                PC=PC_queryset,
                laptop=PC_queryset
            )
            return Laptop_queryset
        except:
            return Response({'detail': 'invalid'})


@api_view(['POST'])
def setReactionAPIView(request, laptop_id, reaction):
    try:
        token = request.META['HTTP_TOKEN']
    except:
        raise AuthenticationFailed('Iltimos, avval tizimga kiring')

    user = checkUserToken(token)
    if not user:
        raise AuthenticationFailed('Iltimos, avval tizimga kiring')

    Laptop_react_status = Laptop.objects.filter(pk=laptop_id, storage=True).exclude(
        author_user=request.user.id).values_list('laptop_reaction').first()

    if Laptop_react_status is None:
        Laptop.objects.filter(pk=laptop_id).update(laptop_reaction=reaction)
        return Response({'detail': 'Reaction set', 'reaction': reaction})

    if Laptop[0] == bool(reaction):
        Laptop.objects.filter(pk=laptop_id).update(laptop_reaction=None)
        return Response({'detail': 'Reaction canceled', 'reaction': None})

    if reaction:
        Laptop.objects.filter(pk=laptop_id).update(laptop_reaction=True)
        return Response({'detail': 'Liked'})

    Laptop.objects.filter(pk=laptop_id).update(laptop_reaction=False)
    return Response({'detail': 'Disliked'})