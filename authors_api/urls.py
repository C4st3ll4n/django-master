from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
#from drf_ysag import openapi
#from drf_ysag.views import get_schema_view

#schema_view = get_schema_view(
#    openapi.Info(
#        title="Authors API",
#        default_version="v1",
#        description="API endpoints for authors",
#        contact=openapi.Contact(email="p13dr0h@gmail.com"),
#        license=openapi.License(name="MIT License")
#    ),
#    public=True,
#    permissions_classes=(permissions.AllowAny,),
#
#)
#
urlpatterns = [
    #path("redoc/", schema_view.with_ui("redoc", cache_timeout=0, name="schema-redoc")   ),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Authors API Admin"
admin.site.site_title = "Authors API Admin Portal"
admin.site.index_title = "Welcome to the Authors API Portal"

