from django.urls import path
from rest_framework.routers import SimpleRouter
from posts.views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)

urlpatterns = router.urls


