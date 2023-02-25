"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from invoice_app .views import dashboard
from profiles.views import login_view
from estimates.views import EstimateFormView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='account_login'),
    path('',dashboard, name='profile_view'),
    path('positions/', include('positions.urls', namespace ='positions')),
    path('invoice_app/', include('invoice_app.urls', namespace ='invoice_app')),
    path('estimates/', include('estimates.urls', namespace ='estimates')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('accounts/',include('allauth.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls'))
]

urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Veedata Invoice panel"
admin.site.index_title = "Veedata Invoice Management"