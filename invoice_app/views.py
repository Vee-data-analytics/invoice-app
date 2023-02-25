
from xml.parsers.expat import model
from django.shortcuts import render, redirect
from positions.models import Position
from profiles.models import Profiles
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from.models import Invoice
from clients.models import Client
from.forms import InvoiceForm
from positions.forms import PositionForm
from django.contrib import messages
from.mixins import InvoiceNoteClosedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
import os
from io import BytesIO
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders


from django.views.generic import (
    ListView,
    FormView,  
    View,
    UpdateView, 
    RedirectView, 
    DeleteView
)


def dashboard(request):
    return render(request, 'dash_plots/analytic_routs.html')
    

class InvoiceListView(ListView):
    model =Invoice
    template_name ="invoice/invoice_index.html"
    paginate_by = 3
    context_object_name = 'qs'
    
    

    def get_queryset(self):
        profile = get_object_or_404(Profiles, user=self.request.user)
        return super().get_queryset().filter(profile=profile).order_by('-created')

class InvoiceFormView(FormView):
    form_class = InvoiceForm
    template_name = 'invoice/create.html'
    i_instance = None

    def get_success_url(self):
        return reverse('invoice_app:detail', kwargs={'pk':self.i_instance.pk})

    def form_valid(self, form):
        profile = Profiles.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)


class AddPositionsFormView(FormView):
    form_class = PositionForm
    template_name = 'invoice/detail.html'

    def get_success_url(self):
        return self.request.path
    
    def form_valid(self, form):
        invoice_pk = self.kwargs.get('pk')
        invoice_obj = Invoice.objects.get(pk=invoice_pk)
        instance = form.save(commit=False)
        instance.invoice = invoice_obj
        form.save()
        messages.info(self.request, f'Successfully added position- {instance.title}')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice_obj = Invoice.objects.get(pk=self.kwargs.get('pk'))
        qs = invoice_obj.positions
        context['obj'] = invoice_obj
        context['qs'] = qs
        return context

class InvoiceUpdateView(LoginRequiredMixin, InvoiceNoteClosedMixin, UpdateView):
    model = Invoice
    template_name = 'invoice/update.html'
    form_class = InvoiceForm
    success_url = reverse_lazy('invoice_app:main')

    def form_valid(self, form):
        instance = form.save()
        messages.info(self.request, f'Successfuly updated invoice - {instance.invoice_number}')
        return super().form_valid(form)


class  CloseInvoiceView(RedirectView ):
    
    pattern_name =  "invoice_app:detail"

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Invoice.objects.get(pk=pk)
        obj.closed = True
        obj.save()
        return super().get_redirect_url(*args, **kwargs)

class  PayedInvoiceView(RedirectView ):
    
    pattern_name =  "invoice_app:detail"

    def get_redirect_url(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Invoice.objects.get(pk=pk)
        obj.payed = True
        obj.save()
        return super().get_redirect_url(*args, **kwargs)


class InvoiceDeleteView(DeleteView):
    
    model = Invoice
    success_url = reverse_lazy('invoice_app:main')
    template_name = 'invoice/invoice_confirm_delete.html'


    def in_delete(request,self,id):
        invoice = Invoice.get_object_or_404(Invoice, id=id)
        invoice.delete()
        #messages.info(self.request, f'Delete position, - {self.object.invoice_number}')
        return redirect(reverse("main"))


class InvoicePositionDeleteView(InvoiceNoteClosedMixin, DeleteView):
    model = Position
    template_name = 'invoice/position_confirm_delete.html'

    def get_object(self):
        pk = self.kwargs.get('position_pk')
        obj = Position.objects.get(pk=pk)
        return obj

    def get_success_url(self):
        messages.info(self.request, f'Delete position, - {self.object.title}')
        return reverse('invoice_app:detail', kwargs={'pk':self.object.invoice.id})



def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
            if not isinstance(result, (list, tuple)):
                    result = [result]
            result = list(os.path.realpath(path) for path in result)
            path=result[0]
    else:
            sUrl = settings.STATIC_URL        # Typically /static/
            sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL         # Typically /media/
            mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/
            if uri.startswith(mUrl):
                    path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                    path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                    return uri
    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path
    

@login_required
def invoices_pdf_print(request, **kwargs):

    pk = kwargs.get('pk')
    obj = Invoice.objects.get(pk=pk)
    
        
    font_result = finders.find('fonts/Lato-Regular.ttf')

    template_path =  'invoice/pdf_print.html'
    context = {
        'object': obj,
        'static': {
            'font': font_result
        },

    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="invoice.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
