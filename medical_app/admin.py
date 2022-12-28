from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from medical_app.models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = UserAdmin.fieldsets + (
            ('Extra Fields', {'fields': ("mobile_no", "gender", "address", "user_type")}),
    )
admin.site.register(CustomUser, CustomUserAdmin)


class PractitionerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Practitioner, PractitionerAdmin)


class NurseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Nurse, NurseAdmin)


class ReceptionistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Receptionist, ReceptionistAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)


class PatientAppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientAppointment, PatientAppointmentAdmin)


class VitalSignAdmin(admin.ModelAdmin):
    pass
admin.site.register(VitalSign, VitalSignAdmin)


class SalesInvoiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(SalesInvoice, SalesInvoiceAdmin)


class InsuranceRecordAdmin(admin.ModelAdmin):
    pass
admin.site.register(InsuranceRecord, InsuranceRecordAdmin)


class MedicalDepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(MedicalDepartment, MedicalDepartmentAdmin)


class PractitionerSpecialityAdmin(admin.ModelAdmin):
    pass
admin.site.register(PractitionerSpeciality, PractitionerSpecialityAdmin)


class ItemGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(ItemGroup, ItemGroupAdmin)


class ItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Item, ItemAdmin)


class PriceListAdmin(admin.ModelAdmin):
    pass
admin.site.register(PriceList, PriceListAdmin)


class ItemPriceAdmin(admin.ModelAdmin):
    pass
admin.site.register(ItemPrice, ItemPriceAdmin)


class ServicesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServicesAdmin)

