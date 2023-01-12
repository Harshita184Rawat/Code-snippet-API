from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from djrest import views
from djrest.views import DjrestViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

djrest_list = DjrestViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
djrest_detail = DjrestViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
djrest_highlight = DjrestViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('djrest/', djrest_list, name='djrest-list'),
    path('djrest/<int:pk>/', djrest_detail, name='djreat-detail'),
    path('djrest/<int:pk>/highlight/', djrest_highlight, name='djrest-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'djrest', views.DjrestViewSet,basename="djrest")
router.register(r'users', views.UserViewSet,basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
    ]