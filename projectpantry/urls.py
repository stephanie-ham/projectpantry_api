from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from projectpantryapi.views import register_user, login_user


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Project: Pantry API",
#         default_version='v1',
#         description="An api for users to buy and sell products",
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),

    # url(r'^swagger(?P<format>\.json|\.yaml)$',
    #     schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # url(r'^swagger/$', schema_view.with_ui('swagger',
    #     cache_timeout=0), name='schema-swagger-ui'),
]
