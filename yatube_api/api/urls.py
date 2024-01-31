from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_ver1 = DefaultRouter()
router_ver1.register(
    'v1/posts',
    PostViewSet,
    basename='posts'
)
router_ver1.register(
    'v1/groups',
    GroupViewSet,
    basename='groups'
)
router_ver1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router_ver1.urls)),
]
