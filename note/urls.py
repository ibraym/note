from django.contrib import admin
from django.urls import path
from .views import list_notes, list_notes_by_category, new_note, new_cat, show_note, edit_note,\
                    delete_note, edit_cat, delete_cat


urlpatterns = [
    # Home Page
    path('', list_notes, name='list-notes'),

    # Note pages
    path('notes/cat/<int:cat_id>/', list_notes_by_category, name='list-note-by-category'),
    path('note/new', new_note, name='new-note'),
    path('note/show/<int:note_id>/', show_note, name='show-note'),
    path('note/edit/<int:note_id>/', edit_note, name='edit-note'),
    path('note/delete/<int:note_id>/', delete_note, name='delete-note'),

    # Category pages
    path('cat/new', new_cat, name='new-cat'),
    path('cat/edit/<int:cat_id>/', edit_cat, name='edit-cat'),
    path('cat/delete/<int:cat_id>/', delete_cat, name='delete-cat'),
]
