from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.get, name="get"),
    path("/", views.fetch_data, name="fetch_data"),
    path("/new", views.new_page, name="new_page"),
    path('/edit', views.edit_page, name='edit_page'),
    path('/saved', views.save_changes, name='save_changes'),
    path('/random', views.random_page, name="random")
]
