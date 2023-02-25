from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView 
from .forms import ClientForm
from profiles.models import Profiles

class CreateClientView(CreateView):
    form_class = ClientForm
    template_name = 'users/new_client.html'

    def get_success_url(self):
        return reverse('estimates:estimate')

    def form_valid(self, form):
        profile = Profiles.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)
