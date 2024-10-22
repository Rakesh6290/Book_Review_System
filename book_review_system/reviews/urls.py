from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:book_pk>/reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
]
