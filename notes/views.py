from django.views.generic import ListView, DetailView, View
from notes.models import Note
from django.shortcuts import render, redirect
from notes.forms import NoteForm
from django.contrib import messages


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note


class NoteAddView(View):
    def get(self, request):
        f = NoteForm()
        return render(request, 'notes/note_new.html', {'form': f})

    def post(self, request):
        f = NoteForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Note successfully saved.')
            return redirect("notes:list")
        else:
            return render(request, 'notes/note_new.html', {'form': f})
