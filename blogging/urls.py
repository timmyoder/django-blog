from django.urls import path, include
from rest_framework import routers
from blogging.views import (
    PostListView,
    PostDetailView,
    UserViewSet,
    CategoryViewSet,
    PostViewSet,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"posts", PostViewSet)
router.register(r"categories", CategoryViewSet)


urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
