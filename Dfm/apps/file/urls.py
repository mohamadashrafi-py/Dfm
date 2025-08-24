from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (  # File Views; Category Views; Tag Views
    FileCategoryCreateView, FileCategoryDeleteView, FileCategoryListView,
    FileCategoryUpdateView, FileCreateView, FileDeleteView, FileListView,
    FileTagCreateView, FileTagDeleteView, FileTagListView, FileTagUpdateView,
    FileUpdateView)

app_name = "file"

urlpatterns = [
    # File URLs
    path("", FileListView.as_view(), name="file_list"),
    path("files/create/", FileCreateView.as_view(), name="file_create"),
    path("files/<int:pk>/update/", FileUpdateView.as_view(), name="file_update"),
    path("files/<int:pk>/delete/", FileDeleteView.as_view(), name="file_delete"),
    # Category URLs
    path("categories/", FileCategoryListView.as_view(), name="category_list"),
    path(
        "categories/create/", FileCategoryCreateView.as_view(), name="category_create"
    ),
    path(
        "categories/<int:pk>/update/",
        FileCategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/<int:pk>/delete/",
        FileCategoryDeleteView.as_view(),
        name="category_delete",
    ),
    # Tag URLs
    path("tags/", FileTagListView.as_view(), name="tag_list"),
    path("tags/create/", FileTagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", FileTagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", FileTagDeleteView.as_view(), name="tag_delete"),
    # Auth
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="file/login.html"),
        name="login",
    ),
]
