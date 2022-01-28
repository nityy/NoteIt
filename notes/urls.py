from django.urls import path
from notes.views import NoteDetailView, NoteListView, NoteAddView

app_name = "notes"
urlpatterns = [
    path('', NoteListView.as_view(), name='list'),
    path('<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path('new/', NoteAddView.as_view(), name='add')
]
