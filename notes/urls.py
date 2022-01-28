from django.urls import path
from notes.views import NoteDeleteView, NoteDetailView, NoteListView, NoteAddView, NoteUpdateView

app_name = "notes"
urlpatterns = [
    path('', NoteListView.as_view(), name='list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path('new/', NoteAddView.as_view(), name='add'),
    path('<int:pk>/edit', NoteUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', NoteDeleteView.as_view(), name='delete')
]
