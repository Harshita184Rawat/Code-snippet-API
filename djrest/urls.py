from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from djrest import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('djrest/',
        views.DjrestList.as_view(),
        name='djrest-list'),
    path('djrest/<int:pk>/',
        views.DjrestDetail.as_view(),
        name='djrest-detail'),
    path('djrest/<int:pk>/highlight/',
        views.DjrestHighlight.as_view(),
        name='djrest-highlight'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
    
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
