from django.urls import path, include
from dash_apps.account import index
from django.contrib.auth.decorators import login_required
from .views import (
invoice_analytics,
analytics_routes,
InvoiceAnalyticView,
payed_invoice)

from dash_apps import (
invoice_plots,
payed_plot)
app_name = 'positions'

urlpatterns = [
    path('analytics/',login_required(invoice_analytics), name='invoice_plot'),
    path('plot/',login_required(InvoiceAnalyticView.as_view()), name='plot'),
    path('payed/',login_required(payed_invoice), name='payed'),
    path('pychart/', login_required(index), name='pychart'),
    path('routes/',login_required(analytics_routes), name='routing')
]
