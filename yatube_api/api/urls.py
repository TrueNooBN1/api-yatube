from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from api.views import PostViewSet, GroupViewSet, CommentViewSet

v1_router = DefaultRouter()
v1_router.register('v1/posts', PostViewSet)
v1_router.register('v1/groups', GroupViewSet)
# Вложенный роутер для комментариев
v1_comments_router = routers.NestedDefaultRouter(v1_router,
                                                 r'v1/posts',
                                                 lookup='post')
v1_comments_router.register(r'comments', CommentViewSet,
                            basename='post-comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls)),
    path('', include(v1_comments_router.urls)),
]
