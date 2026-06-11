from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_main, name='home_main'),
    path('post/<int:id>/', views.home_main_individual, name='blog_individual'),
    path('login/', views.login_u, name='login'),
    path("log/", views.login_user, name="log"),
    path('register/', views.register, name='register'),
    path("reg/", views.register_user, name="register_user"),
    path('logout/', views.logout_user,name='logout'),
    path('home/', views.home, name='home'),
    path('create-post/', views.add, name='create'),
    path("add/", views.create_blog, name="add"),
    path('<int:id>/', views.individual, name='individual'),

]
