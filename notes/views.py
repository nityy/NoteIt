from django.views.generic import ListView, DetailView
from notes.models import Note
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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

# Using generic editing views above
#
# class NoteAddView(View):
#     def get(self, request):
#         f = NoteForm()
#         return render(request, 'notes/note_new.html', {'form': f})

#     def post(self, request):
#         f = NoteForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Note successfully saved.')
#             return redirect("notes:list")
#         else:
#             return render(request, 'notes/note_new.html', {'form': f})
