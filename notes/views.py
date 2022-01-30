from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from notes.models import Note


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note


class NoteAddView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Note
    fields = '__all__'
    template_name_suffix = '_new'
    success_message = "Note successfully saved."

    def get_success_url(self):
        return reverse_lazy('notes:detail', kwargs={'pk': self.object.pk})


class NoteDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('notes:list')
    success_message = "Note successfully deleted."


class NoteUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('notes:detail')
    template_name_suffix = '_update'
    success_message = "Note successfully updated."

    def get_success_url(self):
        return reverse_lazy('notes:detail', kwargs={'pk': self.object.pk})


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    success_message = "Registration Successful"
