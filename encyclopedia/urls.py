from django.urls import path

from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry_page, name="entry_page"),
    path("search_results", views.search_results, name="search_results"),
    path("create_new_page", views.CreatePage.as_view(), name="create_new_page"),
    path("edit_page", views.EditPage.as_view(), name="edit_page"),
    path("random_page", views.random_page, name="random_page")
]
