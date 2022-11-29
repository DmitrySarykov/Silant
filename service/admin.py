from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin
from import_export import resources

# Вид технического обслуживания
class TypeMaintenanceResource(resources.ModelResource):
    class Meta:
        model = TypeMaintenance
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(TypeMaintenance)
class TypeMaintenanceAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = TypeMaintenanceResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Характер отказа
class FailureResource(resources.ModelResource):
    class Meta:
        model = Failure
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(Failure)
class FailureAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = FailureResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Способ восстановления
class RecoveryMethodResource(resources.ModelResource):
    class Meta:
        model = RecoveryMethod
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(RecoveryMethod)
class RecoveryMethodAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = RecoveryMethodResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Сервисная компания
class ServiceCompanyResource(resources.ModelResource):
    class Meta:
        model = ServiceCompany
        report_skipped = True
        fields = ('id','name','description',)

@admin.register(ServiceCompany)
class ServiceCompanyAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ServiceCompanyResource
    list_display = ('id','name','description',)
    filter = ('name',)

# Техническое обслуживание
class MaintenanceResource(resources.ModelResource):
    class Meta:
        model = Maintenance
        report_skipped = True
        fields = ('id','type','date','operating_time','order_number','order_date','service_company','car')

@admin.register(Maintenance)
class MaintenanceAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = MaintenanceResource
    list_display = ('id','type','date','operating_time','order_number','order_date','service_company','car')
    filter = ('date',)

# Рекламация
class ComplaintsResource(resources.ModelResource):
    class Meta:
        model = Complaint
        report_skipped = True
        fields = ('id','date_failure','operating_time','node_failure','description_failure','method_recovery','repair_parts','date_recovery','downtime','car','service_company')

@admin.register(Complaint)
class ComplaintsAdmin(ImportExportMixin,admin.ModelAdmin):
    resource_class = ComplaintsResource
    list_display = ('id','date_failure','operating_time','node_failure','date_recovery','downtime','car','service_company')
    filter = ('date_failure',)