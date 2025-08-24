from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import FileCategoryForm, FileForm, FileTagForm
from .models import FileCategoryModel, FileModel, FileTagModel


# File Views
class FileListView(LoginRequiredMixin, ListView):
    model = FileModel
    template_name = "file/file_list.html"
    paginate_by = 20
    context_object_name = "files"

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        category_filter = self.request.GET.get("category")
        tag_filter = self.request.GET.get("tag")
        search_query = self.request.GET.get("search")

        if category_filter:
            queryset = queryset.filter(category__id=category_filter)

        if tag_filter:
            queryset = queryset.filter(tag__id=tag_filter)

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(category__category__icontains=search_query)
                | Q(tag__tag__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = FileCategoryModel.objects.filter(user=self.request.user)
        context["tags"] = FileTagModel.objects.filter(user=self.request.user)
        return context


class FileCreateView(LoginRequiredMixin, CreateView):
    model = FileModel
    form_class = FileForm
    template_name = "file/file_form.html"
    success_url = reverse_lazy("file:file_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class FileUpdateView(LoginRequiredMixin, UpdateView):
    model = FileModel
    form_class = FileForm
    template_name = "file/file_form.html"
    success_url = reverse_lazy("file:file_list")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = FileModel
    template_name = "file/file_confirm_delete.html"
    success_url = reverse_lazy("file:file_list")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# Category Views
class FileCategoryListView(LoginRequiredMixin, ListView):
    model = FileCategoryModel
    template_name = "file/category_list.html"
    paginate_by = 20
    context_object_name = "categories"

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        # Add search filtering
        search_query = self.request.GET.get("search")
        if search_query:
            queryset = queryset.filter(category__icontains=search_query)

        return queryset


class FileCategoryCreateView(LoginRequiredMixin, CreateView):
    model = FileCategoryModel
    form_class = FileCategoryForm
    template_name = "file/category_form.html"
    success_url = reverse_lazy("file:category_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class FileCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = FileCategoryModel
    form_class = FileCategoryForm
    template_name = "file/category_form.html"
    success_url = reverse_lazy("file:category_list")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class FileCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = FileCategoryModel
    template_name = "file/category_confirm_delete.html"
    success_url = reverse_lazy("file:category_list")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# Tag Views
class FileTagListView(LoginRequiredMixin, ListView):
    model = FileTagModel
    template_name = "file/tag_list.html"
    paginate_by = 20
    context_object_name = "tags"

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)

        # Add search filtering
        search_query = self.request.GET.get("search")
        if search_query:
            queryset = queryset.filter(tag__icontains=search_query)

        return queryset


class FileTagCreateView(LoginRequiredMixin, CreateView):
    model = FileTagModel
    form_class = FileTagForm
    template_name = "file/tag_form.html"
    success_url = reverse_lazy("file:tag_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class FileTagUpdateView(LoginRequiredMixin, UpdateView):
    model = FileTagModel
    form_class = FileTagForm
    template_name = "file/tag_form.html"
    success_url = reverse_lazy("file:tag_list")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class FileTagDeleteView(LoginRequiredMixin, DeleteView):
    model = FileTagModel
    template_name = "file/tag_confirm_delete.html"
    success_url = reverse_lazy("file:tag_list")

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
