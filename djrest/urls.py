from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from djrest import views


urlpatterns = [
    path('djrest/', views.DjrestList.as_view()),
    path('djrest/<int:pk>/', views.DjrestDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)