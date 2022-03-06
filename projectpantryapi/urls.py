from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views as auth_token_views
from django.urls import path, include
from projectpantryapi import views

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.login_user),
    path('register', views.register_user)
]
