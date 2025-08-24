from django import forms

from .models import FileCategoryModel, FileModel, FileTagModel


class FileCategoryForm(forms.ModelForm):
    class Meta:
        model = FileCategoryModel
        fields = ("category",)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(FileCategoryForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(FileCategoryForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance


class FileTagForm(forms.ModelForm):
    class Meta:
        model = FileTagModel
        fields = ("tag",)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(FileTagForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(FileTagForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance


class FileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ("category", "tag", "name", "file")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super(FileForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields["category"].queryset = FileCategoryModel.objects.filter(
                user=self.user
            )
            self.fields["tag"].queryset = FileTagModel.objects.filter(user=self.user)

    def save(self, commit=True):
        instance = super(FileForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
