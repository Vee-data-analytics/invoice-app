from django.contrib import admin
from. models import Client
from import_export import resources
from import_export.admin import ExportActionMixin

class ClientResource(resources.ModelResource):
    class Meta:
        model =Client
        fields = ('id', 'name', 'client_address', 'website', 'vat_no', 'company_reg_no')
        export_order = ('name','website', 'created', 'client_address', 'vat_no', 'company_reg_no', 'id')

class ClientAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = ClientResource

admin.site.register(Client, ClientAdmin)