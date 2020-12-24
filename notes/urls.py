from django.urls import path
from notes.views import NotesList, NoteCreate, NoteUpdate, NoteDelete, TagsList, TagCreate, TagUpdate, TagDelete

urlpatterns = [
    path('', NotesList.as_view(), name='notes'),
    path('add/', NoteCreate.as_view(), name='note-add'),
    path('<int:pk>/edit', NoteUpdate.as_view(), name='note-edit'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='note-delete'),

    path('tags', TagsList.as_view(), name='tags'),
    path('tags/add/', TagCreate.as_view(), name='tag-add'),
    path('tags/<int:pk>/edit', TagUpdate.as_view(), name='tag-edit'),
    path('tags/<int:pk>/delete/', TagDelete.as_view(), name='tag-delete')
]
