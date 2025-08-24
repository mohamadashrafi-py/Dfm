import os

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def user_directory_path(instance, filename):
    return f"files/user_{instance.user.id}/{filename}"


class FileCategoryModel(models.Model):
    """
    Model representing files categories
    """

    category = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="file_categories"
    )

    class Meta:
        verbose_name = "File Category"
        verbose_name_plural = "File Categories"


class FileTagModel(models.Model):
    """
    Model representing files tags
    """

    tag = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_tags")

    class Meta:
        verbose_name = "File Tag"
        verbose_name_plural = "File Tags"


class FileModel(models.Model):
    """
    Model representing files
    """

    category = models.ForeignKey(
        FileCategoryModel, on_delete=models.CASCADE, related_name="file_category"
    )
    tag = models.ManyToManyField(FileTagModel, related_name="file_tag")

    name = models.CharField(max_length=255, unique=True, null=True, blank=True)  # issue
    file = models.FileField(upload_to=user_directory_path)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_files")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "File"
        verbose_name_plural = "Files"

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = os.path.basename(self.file.name)
        super().save(*args, **kwargs)
