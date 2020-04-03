from django.forms import ModelForm
from .models import Note, Category


class NoteForm(ModelForm):
    def create(self):
        if self.is_valid():
            note = self.save(commit=False)

            note.save()
            return True
        return False

    def update(self, note=None):
        if self.is_valid():
            note.title = self.cleaned_data['title']
            note.category = self.cleaned_data['category']
            note.content = self.cleaned_data['content']

            note.save()
            return True
        return False

    class Meta:
        model = Note
        fields = ['title', 'content', 'category']


class CategoryForm(ModelForm):
    def create(self):
        if self.is_valid():
            cat = self.save(commit=False)

            cat.save()
            return True
        return False

    def update(self, cat=None):
        if self.is_valid():
            cat.title = self.cleaned_data['title']

            cat.save()
            return True
        return False

    class Meta:
        model = Category
        fields = ['title']