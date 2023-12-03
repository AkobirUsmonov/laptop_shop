from django.urls import path

from .views import (
    LaptopCreateAPIView,
    PCCreateAPIView,
    PCsListAPIView,
    DeleteAPIView,
    PClaptopListAPIView,
    setReactionAPIView,
)

PC_urlpatterns = [
    path('new-PC', PCCreateAPIView.as_view()),
    path('PC/Laptops', PClaptopListAPIView.as_view()),
    path('PC/<int:user>', PCsListAPIView.as_view()),
    path('PC/delete/<int:PC_id>', DeleteAPIView.as_view())
]

laptop_urlpatterns = [
    path('new-laptop', LaptopCreateAPIView.as_view()),
    path('laptop/react/<int:laptop_id>/<int:reaction>', setReactionAPIView),
]

urlpatterns = PC_urlpatterns + laptop_urlpatterns