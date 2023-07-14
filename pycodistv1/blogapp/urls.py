from django.urls import path

from . import views

app_name = "blogapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("articles/", views.showarticles, name="showarticles"),
    path("<int:article_id>/", views.detailarticle, name="detailarticle"),
    path("<int:account_id>/<str:alias>/", views.changealias, name="changealias"),
    path("newarticle/", views.newarticle, name="newarticle"),
]