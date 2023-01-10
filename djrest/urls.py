from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from djrest import views


urlpatterns = [
    path('djrest/', views.DjrestList.as_view()),
    path('djrest/<int:pk>/', views.DjrestDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]