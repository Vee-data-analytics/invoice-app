from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    InvoiceListView,
    InvoiceFormView,
    InvoiceUpdateView,
    InvoiceUpdateView,
    AddPositionsFormView,
    CloseInvoiceView,
    InvoiceDeleteView,
    InvoicePositionDeleteView,
    PayedInvoiceView,
    invoices_pdf_print,

    
)


app_name = 'invoice_app'

urlpatterns = [
    path('', login_required(InvoiceListView.as_view()), name='main'),
    path('new/', login_required(InvoiceFormView.as_view()), name="create"),
    path('<pk>/', login_required(AddPositionsFormView.as_view()), name='detail'),
    path('<pk>/close/', login_required(CloseInvoiceView.as_view()), name='close'),
    path('<pk>/payed/', login_required(PayedInvoiceView.as_view()), name='payed'),
    path('<pk>/update/', login_required(InvoiceUpdateView.as_view()), name='update'),
    path('<pk>/pdf/', login_required(invoices_pdf_print), name="pdf"),
    path('<pk>/delete/', login_required(InvoiceDeleteView.as_view()), name='invoice-delete'),
    path('<pk>/delete/<int:position_pk>/', login_required(InvoicePositionDeleteView.as_view()), name='position-delete'),
    
]