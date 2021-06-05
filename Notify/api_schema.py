from django.conf.urls import url
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apis.v1 import urls as api_v1

swagger_info = openapi.Info(
    title="Notify API",
    default_version='v1',
    description="This api v1 docs",  # noqa
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="me.shawara@gmail.com"),
    license=openapi.License(name="BSD License"),
)

SchemaView = get_schema_view(
    validators=['ssv', 'flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[url(r"^api/v1/", include((api_v1, "api"), namespace="v1"))],
)
