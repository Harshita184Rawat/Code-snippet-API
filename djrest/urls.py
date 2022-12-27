from django.urls import path
from djrest import views

urlpatterns = [
    path('djrest/', views.djrest_list),
    path('djrest/<int:pk>/', views.djrest_detail),
]