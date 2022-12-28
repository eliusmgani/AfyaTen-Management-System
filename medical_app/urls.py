from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . WebViews import *
from . FuncViews import *

urlpatterns = [
    path("", home, name="home"),
    path("login", login_user, name="login"),
    path("logout", logout_user, name="logout"),
    path("book-appointment", book_appointment, name="book-appointment"),


    # admin-dashboard
    path("admin-dashboard", admin_dashboard, name="admin-dashboard"),
    path("practitioners", PractitonerListView.as_view(), name="practitioners"),
    path("nurses", NurseListView.as_view(), name="nurses"),
    path("receptionists", ReceptionistListView.as_view(), name="receptionists"),
    path("patients", PatientListView.as_view(), name="patients"),
    path("appointments", AppointmentListView.as_view(), name="appointments"),
    path("vitals", AdminVitalListView.as_view(), name="vitals"),
    path("departments", DepartmentListView.as_view(), name="departments"),
    path("specialities", SpecialityListView.as_view(), name="specialities"),
    path("item-groups", ItemGroupListView.as_view(), name="item_groups"),
    path("items", ItemListView.as_view(), name="items"),
    path("price-lists", PriceListListView.as_view(), name="price_lists"),
    path("item-prices", ItemPriceListView.as_view(), name="item_prices"),
    path("services", ServiceListView.as_view(), name="services"),

    #practitioner-dashboard
    path("practitioner-dashboard", practitioner_dashboard, name="practitioner-dashboard"),
    path("pratitioner-patient", PractitionerPatientListView.as_view(), name="practitioner-patient"),

    #nurse-dashboard
    path("nurse-dashboard", nurse_dashboard, name="nurse-dashboard"),
    path("vital-patient", VitalPatientListView.as_view(), name="vital-patient"),
    path("vital-sign", NurseVitalListView.as_view(), name="vital-sign"),

    #receptionist-dashboard
    path("receptionist-dashboard", receptionist_dashboard, name="receptionist-dashboard"),
    path("appointment-patient", AppointmentPatientListView.as_view(), name="appointment-patient"),
    path("patient-appointment", PatientAppointmentListView.as_view(), name="patient-appointment"),


    #Func View
    path("create-patient", CreatePatientView.as_view(), name="create-patient"),
    path("create-patient-appointment", CreatePatientAppointmentView.as_view(), name="create-patient-appointment"),
    path("patient-appointment-detail/<str:pk>", DetailPatientAppointmentView.as_view(), name="patient-appointment-detail"),
    


]



