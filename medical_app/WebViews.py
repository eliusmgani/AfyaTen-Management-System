from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from . models import *

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
    if request.user.is_authenticated:
        return check_user_type(request)
    print(request)
    obj = get_details()
    return render(request, "medical_app/web_view/home.html", {
        "services": obj.get("services"),
        "practitioners": obj.get("practitioners"),
        "departments": obj.get("departments")
    })


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(password)
        print(username)
        print(user)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')

    return render(request, 'medical_app/web_view/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def get_details():
    return {
        "services": Service.objects.filter(image__isnull = False),
        "practitioners": Practitioner.objects.filter(profile_pic__isnull = False), 
        "departments": MedicalDepartment.objects.exclude(description__exact = "")
    }


def book_appointment(request):
    return render(request, "medical_app/web_view/appointment_form.html")


def create_appointment(request):
    pass



class PractitonerListView(LoginRequiredMixin, ListView):
    """Get list of All Practitioners"""

    Model = Practitioner
    context_object_name = "practitioners"
    template_name = "medical_app/user_page/admin_dashboard/practitioner_list.html"

    def get_queryset(self):
        return Practitioner.objects.all()


class NurseListView(LoginRequiredMixin, ListView):
    """Get list of All Nurses"""

    Model = Nurse
    context_object_name = "nurses"
    template_name = "medical_app/user_page/admin_dashboard/nurse_list.html"

    def get_queryset(self):
        return Nurse.objects.all()

class ReceptionistListView(LoginRequiredMixin, ListView):
    """Get list of All Receptionist"""

    Model = Receptionist
    context_object_name = "receptionists"
    template_name = "medical_app/user_page/admin_dashboard/receptionist_list.html"

    def get_queryset(self):
        return Receptionist.objects.all()

class PatientListView(LoginRequiredMixin, ListView):
    """Get list of All Patients"""

    Model = Patient
    context_object_name = "patients"
    template_name = "medical_app/user_page/admin_dashboard/patient_list.html"

    def get_queryset(self):
        return Patient.objects.all()

class AppointmentListView(LoginRequiredMixin, ListView):
    """Get list of All Patient Appointments"""

    Model = PatientAppointment
    context_object_name = "appointments"
    template_name = "medical_app/user_page/admin_dashboard/appointment_list.html"

    def get_queryset(self):
        return PatientAppointment.objects.all()

class AdminVitalListView(LoginRequiredMixin, ListView):
    """Get list of All Vital Signs"""

    Model = VitalSign
    context_object_name = "vitals"
    template_name = "medical_app/user_page/admin_dashboard/vital_list.html"

    def get_queryset(self):
        return VitalSign.objects.all()

class DepartmentListView(LoginRequiredMixin, ListView):
    """Get list of All Depertments"""

    Model = MedicalDepartment
    context_object_name = "departments"
    template_name = "medical_app/user_page/admin_dashboard/department_list.html"

    def get_queryset(self):
        return MedicalDepartment.objects.all()

class SpecialityListView(LoginRequiredMixin, ListView):
    """Get list of All Specialities"""

    Model = PractitionerSpeciality
    context_object_name = "specialities"
    template_name = "medical_app/user_page/admin_dashboard/speciality_list.html"

    def get_queryset(self):
        return PractitionerSpeciality.objects.all()

class ItemGroupListView(LoginRequiredMixin, ListView):
    """Get list of All Item Groups"""

    Model = ItemGroup
    context_object_name = "item_groups"
    template_name = "medical_app/user_page/admin_dashboard/item_group_list.html"

    def get_queryset(self):
        return ItemGroup.objects.all()

class ItemListView(LoginRequiredMixin, ListView):
    """Get list of All Items"""

    Model = Item
    context_object_name = "items"
    template_name = "medical_app/user_page/admin_dashboard/items_list.html"

    def get_queryset(self):
        return Item.objects.all()

class PriceListListView(LoginRequiredMixin, ListView):
    """Get list of All Price Lists"""

    Model = PriceList
    context_object_name = "price_lists"
    template_name = "medical_app/user_page/admin_dashboard/price_list.html"

    def get_queryset(self):
        return PriceList.objects.all()

class ItemPriceListView(LoginRequiredMixin, ListView):
    """Get list of All Item Price"""

    Model = ItemPrice
    context_object_name = "item_prices"
    template_name = "medical_app/user_page/admin_dashboard/item_price_list.html"

    def get_queryset(self):
        return ItemPrice.objects.all()

class AppointmentPatientListView(LoginRequiredMixin, ListView):
    """Get list of All Patients in Receptionist Dashboard"""

    Model = Patient
    context_object_name = "patients"
    template_name = "medical_app/user_page/receptionist_dashboard/patient_list.html"

    def get_queryset(self):
        return Patient.objects.all()

class VitalPatientListView(LoginRequiredMixin, ListView):
    """Get list of All Patients in Nurse Dashboard"""

    Model = Patient
    context_object_name = "patients"
    template_name = "medical_app/user_page/nurse_dashboard/patient_list.html"

    def get_queryset(self):
        return ItemPrice.objects.all()

class PractitionerPatientListView(LoginRequiredMixin, ListView):
    """Get list of All Patients in Practitioner Dashboard"""

    Model = Patient
    context_object_name = "patients"
    template_name = "medical_app/user_page/practitioner_dashboard/patient.html"

    def get_queryset(self):
        return Patient.objects.all()  

class ServiceListView(LoginRequiredMixin, ListView):
    """Get list of All Services"""

    Model = Service
    context_object_name = "services"
    template_name = "medical_app/user_page/admin_dashboard/service_list.html"

    def get_queryset(self):
        return Service.objects.all()

def check_user_type(request):
    if request.user.user_type == "Practitioner":
        return redirect("practitioner-dashboard")

    elif request.user.user_type == "Nurse":
        return redirect("nurse-dashboard")

    elif request.user.user_type == "Receptionist":
        return redirect("receptionist-dashboard")

    else:
        return redirect("admin-dashboard")

def admin_dashboard(request):
    return render(request, "medical_app/user_page/admin_dashboard/admin_dashboard.html")

def practitioner_dashboard(request):
    return render(request, "medical_app/user_page/practitioner_dashboard/practitioner_dashboard.html")
    
def nurse_dashboard(request):
    return render(request, "medical_app/user_page/nurse_dashboard/nurse_dashboard.html")

def receptionist_dashboard(request):
    return render(request, "medical_app/user_page/receptionist_dashboard/receptionist_dashboard.html")

class PatientAppointmentListView(LoginRequiredMixin, ListView):
    """Get list of All Appointments in Receptionist Dashbaoard"""

    Model = PatientAppointment
    context_object_name = "patient_appointments"
    template_name = "medical_app/user_page/receptionist_dashboard/patient_appointment_list.html"

    def get_queryset(self):
        return PatientAppointment.objects.all()

class NurseVitalListView(LoginRequiredMixin, ListView):
    """Get list of All Vitals in Nurse Dashboard"""

    Model = VitalSign
    context_object_name = "vitals"
    template_name = "medical_app/user_page/nurse_dashboard/vital_sign.html"

    def get_queryset(self):
        return VitalSign.objects.all()  