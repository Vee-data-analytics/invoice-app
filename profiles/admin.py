from django.contrib import admin
from.models import Profiles
from import_export import resources
from import_export.fields import Field 
from import_export.admin import ExportActionMixin

class ProfilesResource(resources.ModelResource):
    user = Field()
    class Meta:
        model = Profiles
        fields = (' id','user','account_number','company_name','company_address','created_date','updated_dated')

        def dehydrate_user(self, obj):
            return obj.user.username

class ProfileAdmin(ExportActionMixin,admin.ModelAdmin):
    resource_class = ProfilesResource


admin.site.register(Profiles)
