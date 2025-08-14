from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet, basename='posts')
router.register(prefix='comments', viewset=PostViewSet, basename='comments')

urlpatterns = router.urls
