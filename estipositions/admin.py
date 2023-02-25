from django.contrib import admin
from pandas import describe_option
from .models import Position
from import_export import resources
from import_export.fields import Field
from import_export.admin import ExportActionMixin

class PositionResource(resources.ModelResource):
    estimate = Field()
    description = Field()
    class Meta:
        model = Position
        fields = ('id', 'invoice', 'title', 'description')

    def dehydrate_invoice(self, obj):
        return obj.estimate.number
    

    def dehydrate_position(self,obj):
        if obj.description == "":
            return"-"
        return obj.description

class PositionAdmin( ExportActionMixin ,admin.ModelAdmin):
    resource_class = PositionResource

admin.site.register(Position, PositionAdmin)