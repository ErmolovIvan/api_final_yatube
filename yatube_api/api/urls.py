from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PostViewSet, CommentViewSet, FollowViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
