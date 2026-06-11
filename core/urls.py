from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path("log/", views.login_user, name="log"),
    path('register/', views.register, name='register'),
    path("reg/", views.register_user, name="register_user"),
    path('home/', views.home, name='home'),
    path('create-post/', views.create_blog, name='create'),
    path("add/", views.add, name="add"),
    path('<int:id>/', views.individual, name='individual'),
]