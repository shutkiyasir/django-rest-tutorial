from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

router = DefaultRouter()
router.register(r"users", views.UserViewset, basename="user")
router.register(r"snippets", views.SnippetViewset, basename="snippet")

from snippets import views

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
