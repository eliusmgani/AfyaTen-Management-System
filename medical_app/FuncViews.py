from . models import Patient, PatientAppointment
from . forms import PatientForm, PatientAppointmentForm
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.shortcuts import redirect

class CreatePatientView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    fields = "__all__"

    template_name = "medical_app/user_page/receptionist_dashboard/patient_form.html"
    success_url = reverse_lazy("patients")
    success_message = "Patient created successfully..!!"

class CreatePatientAppointmentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PatientAppointment
    form_class = PatientAppointmentForm
    template_name = "medical_app/user_page/receptionist_dashboard/patient_appointment_form.html"
    success_url = reverse_lazy("patient-appointment-detail")
    success_message = "Patient Appointment created successfully..!!"

    # def form_valid(self, form):
        # Do something with the form data

        # form.save()
        # return super().form_valid(form)

class DetailPatientAppointmentView(LoginRequiredMixin, DetailView):
    model = PatientAppointment
    template_name = "medical_app/user_page/func_view_page/patient_appointment_detail.html"
