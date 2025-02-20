from django.urls import path
from . import views
from django.conf.urls.static import static
from . import settings

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_blog, name="add_blog"),
    path("read/", views.read_blog, name="read_blog"),
    path("detail/<blog_id>/", views.detail_blog, name="detail_blog"),
    path("update/<blog_id>/", views.update_blog, name="update_blog"),
    path("delete/<blog_id>/", views.delete_blog, name="delete_blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
