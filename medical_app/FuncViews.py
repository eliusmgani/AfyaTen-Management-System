from . models import Patient, PatientAppointment
from . forms import PatientForm, PatientAppointmentForm
from django.views.generic import (
    CreateView, UpdateView, DeleteView, DetailView,
    ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.shortcuts import redirect, render


def func_view_dashboard(request):
    return render(request, "medical_app/user_page/func_view_page/func_view_dashboard.html")



class PatientListView(LoginRequiredMixin, ListView):
    """Get list of All Patients"""

    Model = Patient
    context_object_name = "patients"
    template_name = "medical_app/user_page/func_view_page/patient_list.html"

    def get_queryset(self):
        return Patient.objects.all()

class CreatePatientView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create Patient"""

    model = Patient
    form_class = PatientForm
    template_name = "medical_app/user_page/func_view_page/patient_form.html"
    success_url = reverse_lazy("patients")
    success_message = "%(full_name)s created successfully..!!"

class AppointmentListView(LoginRequiredMixin, ListView):
    """Get list of All Patient Appointments"""

    Model = PatientAppointment
    context_object_name = "appointments"
    template_name = "medical_app/user_page/func_view_page/patient_appointment_list.html"

    def get_queryset(self):
        return PatientAppointment.objects.all()

class CreatePatientAppointmentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create Patient Appointment"""
    model = PatientAppointment
    form_class = PatientAppointmentForm
    template_name = "medical_app/user_page/func_view_page/patient_appointment_form.html"
    success_url = reverse_lazy("patient-appointment-detail")
    success_message = "Patient Appointment: %(name)s created successfully..!!"

    # def form_valid(self, form):
        # Do something with the form data

        # form.save()
        # return super().form_valid(form)

class DetailPatientAppointmentView(LoginRequiredMixin, DetailView):
    model = PatientAppointment
    template_name = "medical_app/user_page/func_view_page/patient_appointment_detail.html"
