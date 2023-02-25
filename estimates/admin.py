from django.contrib import admin
from xmlrpc import client
from django.contrib import admin
from .models import Estimate
from django.contrib import admin
from django.dispatch import receiver
from .models import Estimate, Tag
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

class TagResource(resources.ModelResource):
    class Meta:
        model = Tag
        fields = ('id', 'name')

    
class TagAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = TagResource

class EstimateResource(resources.ModelResource):
    profile = Field()
    client = Field()
    created = Field()
    closed = Field()
    positions = Field()
    total_amount = Field()

    class Meta:
        model = Estimate
        fields = ("id", "profile", "clients", "number", "completion_date", "issue_date", "payment_date", "created", "closed", "positions", "total_amount")

    def dehydrate_profile(self, obj):
        return obj.profile.user.username

    def dehydrate_receiver(self, obj):
        return obj.client .name

    def dehydrate_created(self, obj):
        return obj.created.strftime("%d-%m-%y")

    def dehydrate_closed(self, obj):
        if obj.closed == True:
            return "True"
        else: return "False"

    def dehydrate_positions(self, obj):
        positions_list = [x.title for x in obj.positions]
        positions_string = ", ".join(positions_list)
        return positions_string

    def dehydrate_total_amount(self, obj):
        return obj.total_amount

    

class EstimateAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = EstimateResource

admin.site.register(Estimate, EstimateAdmin)
admin.site.register(Tag, TagAdmin)

