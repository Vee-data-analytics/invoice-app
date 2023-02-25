from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect,  get_object_or_404
from profiles.forms import ProfileForm
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Profiles
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

def get_profile(user):
    qs = Profiles.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def login_view(request):
    return render( request, 'account/login.html')

def logout_view(request):
    return render(request, 'account/logout.html')

def signup_view(request):
    return render(request, 'account/signup.html')




def profile(request, **kwargs):

    id = kwargs.get('id')
    obj = Profiles.objects.get(id=id)
    

    template_path =  'users/profile.html'
    context = {
        'object': obj,

    }
    return render(request, template_path, context)


class ProfileDetailView(LoginRequiredMixin,DetailView):
    template_name = 'users/profile.html'
    queryset = User.objects.all()
    success_url = '/'

    def get_object(self):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        return user
    
    def get_context_data(self, **kwargs):
        users = Profiles.objects.all()
        context = super().get_context_data(**kwargs)
        context['users'] = users



class CreateProfileView(CreateView):
    form_class = ProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse('invoice_app:main')

    def form_valid(self, form):
        profile = Profiles.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        messages.info(self.request, 'Successfuly createted Proifile' )
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    model = Profiles
    template_name = 'invoice/update.html'
    form_class = ProfileForm
    success_url = reverse_lazy('invoice_app:main')

    def get_object(self):
        id_ = self.kwargs.get('username')
        return get_object_or_404(User, username=id_ )

    def form_vaild(self,request, form):
        form.instance.employee = get_profile(self.request.user)
        form.save()
        messages.success(request, f'Your account was successfully updated')
        return redirect(reverse('profiles:profile_de', kwargs={
            'username': form.instance.username
            }))
