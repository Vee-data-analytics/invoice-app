from django.shortcuts  import  redirect
from .models import Estimate 

class EstimateNoteClosedMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = Estimate.objects.get(pk=kwargs.get('pk'))
        if obj.closed:
            return redirect('estimates:main')
        return super().dispatch(request, *args, **kwargs)