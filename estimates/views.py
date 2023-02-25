from xml.parsers.expat import model
from django.shortcuts import render, redirect
from positions.models import Position
from profiles.models import Profiles
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from.models import Estimate
from.forms import EstimateForm
from estipositions.forms import EstimatePositionForm
from django.contrib import messages
from.mixins import EstimateNoteClosedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic import (
    ListView,
    FormView,  
    DetailView,
    UpdateView, 
    RedirectView, 
    DeleteView
)


class EstimateListView(ListView):
    model =Estimate
    template_name ="estimates/estimate_index.html"
    paginate_by = 3
    context_object_name = 'qs'
    

    def get_queryset(self):
        profile = get_object_or_404(Profiles, user=self.request.user)
        return super().get_queryset().filter(profile=profile).order_by('-created')

class EstimateFormView(FormView):
    form_class = EstimateForm
    template_name = 'estimates/create_estimate.html'
    i_instance = None

    def get_success_url(self):
        return reverse('estimates:estimate_detail', kwargs={'pk':self.i_instance.pk})

    def form_valid(self, form):
        profile = Profiles.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)

class EstimateDeleteView(DeleteView):
    
    model = Estimate
    success_url = reverse_lazy('estimates:main')
    template_name = 'invoice/invoice_confirm_delete.html'

    def in_delete(request,self,id):
        estimate = Estimate.get_object_or_404(Estimate, id=id)
        estimate.delete()
        #messages.info(self.request, f'Delete position, - {self.object.invoice_number}')
        return redirect(reverse("estimates:main"))


class AddPositionsFormView(FormView):
    form_class = EstimatePositionForm
    template_name = 'estimates/detail.html'

    def get_success_url(self):
        return self.request.path
    
    def form_valid(self, form):
        estimate_pk = self.kwargs.get('pk')
        estimate_obj = Estimate.objects.get(pk=estimate_pk)
        instance = form.save(commit=False)
        instance.estimate = estimate_obj
        form.save()
        messages.info(self.request, f'Successfully added position- {instance.title}')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estimate_obj = Estimate.objects.get(pk=self.kwargs.get('pk'))
        qs = estimate_obj.positions
        context['obj'] = estimate_obj
        context['qs'] = qs
        return context

class EstimateUpdateView(LoginRequiredMixin, EstimateNoteClosedMixin, UpdateView):
    model = Estimate
    template_name = 'estimates/update.html'
    form_class = EstimateForm
    success_url = reverse_lazy('estimates:main')

    def form_valid(self, form):
        instance = form.save()
        messages.info(self.request, f'Successfuly updated estimate - {instance.estimate_number}')
        return super().form_valid(form)


class CloseEstimateView(RedirectView ):
    
    pattern_name =  "estimates:estimate_detail"

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Estimate.objects.get(pk=pk)
        obj.closed = True
        obj.save()
        return super().get_redirect_url(*args, **kwargs)

class EstimatePositionDeleteView(EstimateNoteClosedMixin, DeleteView):
    model = Position
    template_name = 'estimate/position_confirm_delete.html'

    def get_object(self):
        pk = self.kwargs.get('position_pk')
        obj = Position.objects.get(pk=pk)
        return obj

    def get_success_url(self):
        messages.info(self.request, f'Delete position, - {self.object.title}')
        return reverse('estimate:detail', kwargs={'pk':self.object.estimtae.id})


def estimate_pdf_print(request, **kwargs):
    pk = kwargs.get('pk')
    obj = Estimate.objects.get(pk=pk)

    logo_result =finders.find('img/zibi_logo.png')
    font_result = finders.find('fonts/Lato-Regular.ttf')
    searched_locations = finders.searched_locations
    print(searched_locations)

    template_path =  'estimates/pdf_print.html'
    
    context = {
        'object': obj,
        'static': {
            'font': font_result,
            'logo': logo_result,
        },
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="estimate.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
       html.encode('utf-8'), dest=response, encoding='utf-8')

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response