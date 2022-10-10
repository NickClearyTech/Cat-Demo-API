from django.urls import include, path
from rest_framework import routers
from demoapp import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r"cat", views.CatViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
