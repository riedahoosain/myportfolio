from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

from .models import Notes
from .forms import NotesForm


class NotesDeleteView(DeleteView):
    '''Deletes a Note'''
    model = Notes
    success_url = '/smart/notes'
    template_name = "notes/notes_delete.html"



class NotesUpdateView(UpdateView):
    '''Updates a Note'''
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = "notes/notes_form.html"


class NotesCreateView(CreateView):
    '''Creates a Note'''
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = "notes/notes_form.html"


class NotesListView(ListView):
    '''Lists the Notes'''
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    '''Lists Detailed Note'''
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_detail.html"
