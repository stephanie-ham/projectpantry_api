from rest_framework.routers import DefaultRouter
from django.urls import path, include
from projectpantryapi import views

router = DefaultRouter(trailing_slash=False)
router.register(r'foods', views.FoodView, 'food')
router.register(r'locations', views.LocationView, 'location')
router.register(r'quantities', views.QuantityView, 'quantity')
router.register(r'tags', views.TagView, 'tag')

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.login_user),
    path('register', views.register_user)
]
