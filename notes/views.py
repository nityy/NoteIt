from django.views.generic import ListView, DetailView, View
from notes.models import Note
from django.shortcuts import render
from notes.forms import NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


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
            return HttpResponseRedirect(reverse("notes:list"))
