from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, TagViewSet

router = DefaultRouter()
router.register(prefix='posts', viewset=PostViewSet, basename='posts')
router.register(prefix='comments', viewset=CommentViewSet, basename='comments')
router.register(prefix='tags', viewset=TagViewSet, basename='tags')

urlpatterns = router.urls
