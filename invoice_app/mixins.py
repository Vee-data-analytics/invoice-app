from django.shortcuts  import  redirect
from .models import Invoice 

class InvoiceNoteClosedMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = Invoice.objects.get(pk=kwargs.get('pk'))
        if obj.closed:
            return redirect('invoice_app:main')
        return super().dispatch(request, *args, **kwargs)