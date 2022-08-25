from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Authors API",
        default_version="v1",
        description="API endpoints for authors",
        contact=openapi.Contact(email="p13dr0h@gmail.com"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("djoser.urls.jwt")),
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
    path("api/v1/articles/", include("core_apps.articles.urls")),
    path("api/v1/ratings/", include("core_apps.ratings.urls")),
    path("api/v1/vote/", include("core_apps.reactions.urls")),
    path("api/v1/favorite/", include("core_apps.favorites.urls")),
    path("api/v1/comments/", include("core_apps.comments.urls")),
    path("api/v1/haystack/", include("core_apps.search.urls")),
]

admin.site.site_header = "Authors API Admin"
admin.site.site_title = "Authors API Admin Portal"
admin.site.index_title = "Welcome to the Authors API Portal"
