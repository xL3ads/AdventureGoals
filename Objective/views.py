from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from Objective.forms import ObjectiveForm
from Objective.models import Objective


# Create your views here.
class ObjectiveCreateView(LoginRequiredMixin, CreateView):
    template_name = 'Objective/create_objective.html'
    model = Objective
    form_class = ObjectiveForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['user'] = self.request.user
        
        return data
    
    def form_valid(self, form):
        user = self.request.user
        
        # VALIDARE DUPA TITLU
        # titlul introdus
        get_title = form.cleaned_data['title']
        # verificam daca a mai fost intrdus de catre user
        objective_filter = Objective.objects.filter(user=user, title=get_title)
        if objective_filter:
            msg = f'Objective {get_title} already exists'
            form.add_error('title', msg)
            return self.form_invalid(form)
        
        # Pastram instanta userului
        
        form.instance.user = user
        return super().form_valid(form)

class ObjectiveListView(LoginRequiredMixin, ListView):
    template_name = 'Objective/list_objectives.html'
    model = Objective
    context_object_name = 'objectives'

    def get_queryset(self):
        return Objective.objects.filter(user=self.request.user)
            
        