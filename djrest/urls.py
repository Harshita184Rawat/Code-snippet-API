from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from djrest import views


urlpatterns = [
    path('djrest/', views.djrest_list),
    path('djrest/<int:pk>/', views.djrest_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)