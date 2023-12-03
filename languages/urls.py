from django.urls import path

from .views import LaptopsAndPCsListAPIView

urlpatterns = [
    path('lang', LaptopsAndPCsListAPIView.as_view()),
]