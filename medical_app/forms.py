# from django.forms import forms
from django.forms import (
    ModelForm,
    DateInput,
    EmailInput,
    TextInput,
    NumberInput,
    Select,
    Textarea
)
from . models import *

choices = (
    ("", ""),
    ("Male", "Male"),
    ("Female", "Female")
)

class PatientForm(ModelForm):
    
    class Meta:
        model = Patient
        fields = "__all__"
    
        widgets = {
            "full_name": TextInput(attrs={
                "type": "text",
                "placeholder": "full name",
                "size": "60px"
            }),
            "email": EmailInput(attrs={
                "type": "email",
                "placeholder": "email",
                "size": "60px"
            }),
            "mobile_no": NumberInput(attrs={
                "type": "number",
                "placeholder": "mobile number",
                "size": "60px"
            }),
            "gender": Select(
                choices=choices,
                attrs={
                    "type": "text",
                    "placeholder": "gender",
                    "style": "width:150px"
                }
            ),
            "date_of_birth": DateInput(attrs={
                "type": "date",
                "style": "width:150px"
            }),
            "address": Textarea(attrs={
                "placeholder": "Address",
                "cols": 40,
                "rows": 5
            })
        }


class PatientAppointmentForm(ModelForm):
    
    class Meta:
        model = PatientAppointment
        fields = "__all__"
        exclude = ["name"]

        widgets = {
            "gender": Select(
                choices=choices,
                attrs={
                    "type": "text",
                    "placeholder": "gender",
                    "style": "width:150px"
            }),
            "coverage_plan": TextInput(attrs={
                "type": "text",
                "placeholder": "coverage plan",
                "size": "60px"
            }),
            "cardno": TextInput(attrs={
                "type": "text",
                "placeholder": "card number",
                "size": "60px"
            }),
            "insurance_company": TextInput(attrs={
                "type": "text",
                "placeholder": "Insurance Company",
                "size": "60px"
            }),
            "authorization_no": TextInput(attrs={
                "type": "text",
                "placeholder": "authorization number",
                "size": "60px"
            }),
            "invoice_no": TextInput(attrs={
                "type": "text",
                "placeholder": "invoice number",
                "size": "60px"
            }),
            "billing_item": TextInput(attrs={
                "type": "text",
                "placeholder": "billing item",
                "size": "60px"
            }),
            "amount": TextInput(attrs={
                "type": "number",
                "placeholder": "amount",
                "size": "60px"
            })
        }
    
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