from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from matplotlib.style import context
from estimates.models import  Estimate
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from positions.models import Position
from invoice_app.models import Invoice
from estipositions.models import Position as EstaPos
from profiles.models import Profiles
from django.db.models import F
from django.contrib.auth.models import User

class EstimateAnalyticView(View):
    model =Estimate
    template_name ="dash_plots/estimate_plot.html"
    context_object_name = 'qs'


    def get_queryset(self):
        profile = get_object_or_404(Profiles, user=self.request.user)
        return super().get_queryset().filter(profile=profile).order_by('-created')



class InvoiceAnalyticView(View):
    model =Estimate
    template_name ='dash_plots/invoice_plot.html'
    context_object_name = 'qs'


    def get_queryset(self):
        profile = get_object_or_404(Profiles, user=self.request.user)
        return super().get_queryset().filter(profile=profile).order_by('-created')

@login_required
def analytics_routes(request):
    return render (request,'dash_plots/analytic_routs.html')

@login_required
def invoice_analytics(request):
    current_user = request.user
    qs = Position.objects.filter(current_user)
    context={
        qs:'qs'
    }
    return render (request,'dash_plots/invoice_plot.html',context)

@login_required
def payed_invoice(request):
    current_user = request.user
    qs = Position.objects.filter(current_user)
    context={
        qs:'qs'
    }
    return render (request,'dash_plots/payed_invoice.html', context)


"""Entry.objects.filter(authors__name=F('blog__name'))
"""
