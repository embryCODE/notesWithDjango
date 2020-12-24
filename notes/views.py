from django import forms
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from notes.models import Note, Tag


class NotesList(ListView):
    model = Note


class TagsList(ListView):
    model = Tag


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'content', 'tags']

    def get_form(self, form_class=None):
        tag_choices = ((x.id, x.name) for x in Tag.objects.all())
        form = super(NoteCreate, self).get_form(form_class)
        form.fields['tags'].widget = forms.CheckboxSelectMultiple(choices=tag_choices)

        return form

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('notes')


class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'content', 'tags']

    def get_form(self, form_class=None):
        tag_choices = ((x.id, x.name) for x in Tag.objects.all())
        form = super(NoteUpdate, self).get_form(form_class)
        form.fields['tags'].widget = forms.CheckboxSelectMultiple(choices=tag_choices)

        return form

    def get_success_url(self):
        return reverse('notes')


class NoteDelete(DeleteView):
    model = Note
    success_url = reverse_lazy('/')

    def get_success_url(self):
        return reverse('notes')


class TagCreate(CreateView):
    model = Tag
    fields = ['name']

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tags')


class TagUpdate(UpdateView):
    model = Tag
    fields = ['name']

    def get_success_url(self):
        return reverse('tags')


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('/tags')

    def get_success_url(self):
        return reverse('tags')
