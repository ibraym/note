from django.shortcuts import render, redirect
from .models import Note, Category
from .forms import NoteForm, CategoryForm
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# Note Views
def list_notes(request):
    cats = Category.objects.all()
    notes = Note.objects.all()
    context = {'notes': notes, 'cats': cats}
    return render(request, 'home.html', context)


def list_notes_by_category(request, cat_id):
    cats = Category.objects.all()
    # Check category exists
    try:
        cat = Category.objects.filter(id=cat_id).get()
        notes = Note.objects.filter(category=cat_id)
        context = {'notes': notes, 'cats': cats, 'cat': cat}
        return render(request, 'home.html', context)
    except:
        messages.error(request, 'Category does not exist!')
        return redirect('list-notes')


def new_note(request):
    cats = Category.objects.all()
    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.create():
            messages.success(request, 'Note has been added successfully!.')
            return redirect('list-notes')
    context = {'form': form, 'cats': cats}
    return render(request, 'note/new.html', context)


def show_note(request, note_id):
    cats = Category.objects.all()
    # Check note exists
    try:
        note = Note.objects.filter(id=note_id).get()
        context = {'note': note, 'cats': cats}
        return render(request, 'note/show.html', context)
    except:
        messages.error(request, 'Note does not exist!')
        return redirect('list-notes')


def edit_note(request, note_id):
    cats = Category.objects.all()
    # Check note exists
    try:
        note = Note.objects.filter(id=note_id).get()
    except:
        messages.error(request, 'Note does not exist!')
        return redirect('list-notes')

    if request.method != 'POST':
        form = NoteForm(data={
            'title': note.title,
            'category': note.category,
            'content': note.content,
        })
    else:
        form = NoteForm(data=request.POST)

        if form.update(note):
            messages.success(request, 'Note has been updated successfully!.')
            return HttpResponseRedirect(reverse('show-note', kwargs={'note_id': note_id}))

    context = {'form': form, 'cats': cats, 'note': note}
    return render(request, 'note/edit.html', context)


def delete_note(request, note_id):
    cats = Category.objects.all()
    # Check note exists
    try:
        note = Note.objects.filter(id=note_id).get()
    except:
        messages.error(request, 'Note does not exist!')
        return redirect('list-notes')

    if note.delete():
        messages.success(request, 'Note has been deleted successfully!.')
        return HttpResponseRedirect(reverse('list-notes'))


# Category Views
def new_cat(request):
    cats = Category.objects.all()
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.create():
            messages.success(request, 'Category has been added successfully!.')
            return redirect('list-notes')
    context = {'form': form, 'cats': cats}
    return render(request, 'category/new.html', context)


def edit_cat(request, cat_id):
    cats = Category.objects.all()
    # Check category exists
    try:
        cat = Category.objects.filter(id=cat_id).get()
    except:
        messages.error(request, 'Category does not exist!')
        return redirect('list-notes')

    if request.method != 'POST':
        form = CategoryForm(data={'title': cat.title})
    else:
        form = CategoryForm(data=request.POST)

        if form.update(cat):
            messages.success(request, 'Category has been updated successfully!.')
            return HttpResponseRedirect(reverse('list-note-by-category', kwargs={'cat_id': cat_id}))

    context = {'form': form, 'cats': cats, 'cat': cat}
    return render(request, 'category/edit.html', context)


def delete_cat(request, cat_id):
    cats = Category.objects.all()
    # Check category exists
    try:
        cat = Category.objects.filter(id=cat_id).get()
    except:
        messages.error(request, 'Category does not exist!')
        return redirect('list-notes')

    if cat.delete():
        messages.success(request, 'Category has been deleted successfully!.')
        return HttpResponseRedirect(reverse('list-notes'))