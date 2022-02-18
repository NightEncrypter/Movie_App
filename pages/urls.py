from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# From all import from views
from . import views

# import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    # path("register", views.register, name="register"),
    path("movie/<str:movie_id>", views.movie, name="movie"),
    path("cat", views.cat, name="cat"),
    # path("login", views.login, name="login")
]+  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
