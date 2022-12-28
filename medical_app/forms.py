# from django.forms import forms
from django.forms import ModelForm
from . models import *

def PatientForm(ModelForm):
    
    class Meta:
        model = Patient
        fields = "__all__"

    # def clean(self):
    #     cleaned_data = super().clean()

class PatientAppointmentForm(ModelForm):
    
    class Meta:
        model = PatientAppointment
        fields = "__all__"
        exclude = ["name"]
    
    def clean(self):
        cleaned_data = super().clean()
        is_cash_patient = cleaned_data.get("is_cash_patient")
        insurance_subscription = cleaned_data.get("insurance_subscription")
        insurance_company = cleaned_data.get("insurance_company")
        coverage_plan = cleaned_data.get("coverage_plan")
        cardno = cleaned_data.get("cardno")
        invoice_no = cleaned_data.get("invoice_no")
        
        errors = []
        if is_cash_patient == False:
            if not insurance_subscription:
                errors.append({"insurance_subscription": "Insurance Subscription is mandatory"})
            if not insurance_company:
                errors.append({"insurance_company": "Insurance company is mandatory"})
            if not coverage_plan:
                errors.append({"coverage_plan": "Coverage plan is mandatory"})
            if not cardno:
                errors.append({"cardno": "cardno is mandatory"})
        else:
            if not invoice_no:
                errors.append({"invoice_no": "Invoice No is mandatory"})
        
        if len(errors) > 0:
            self.add_error(None, errors)