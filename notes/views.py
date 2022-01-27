from django.views.generic import ListView, DetailView
from notes.models import Note
# Create your views here.


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'


class NoteDetailView(DetailView):
    model = Note
