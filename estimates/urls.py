from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    EstimateListView,
    EstimateFormView,
    EstimateUpdateView,
    AddPositionsFormView,
    CloseEstimateView,
    EstimateDeleteView,
    EstimatePositionDeleteView,
    estimate_pdf_print,
)

app_name = 'estimates'

urlpatterns = [
    path('', login_required(EstimateListView.as_view()), name='main'),
    path('new/',login_required(EstimateFormView.as_view()), name="estimate"),
    path('<pk>/', login_required(AddPositionsFormView.as_view()), name='estimate_detail'),
    path('<pk>/close/', login_required(CloseEstimateView.as_view()), name='close'),
    path('<pk>/update/', login_required(EstimateUpdateView.as_view()), name='estimate-update'),
    path('<pk>/delete/', login_required(EstimateDeleteView.as_view()), name='estimate-delete'),
    path('<pk>/pdf/', login_required(estimate_pdf_print), name="pdf"),
    path('<pk>/delete/<int:position_pk>/', login_required(EstimatePositionDeleteView.as_view()), name='position-delete'),
]