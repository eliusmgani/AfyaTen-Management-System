from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.utils import timezone

from . utils import get_abbr, get_date_str_combined, count_data

user_type_data = (
		("Admin", "Admin"),
		("Practitioner", "Practitioner"),
        ("Nurse", "Nurse"),
        ("Receptionist", "Receptionist")
	)

patient_abdomen_type = (
		("Normal", "Normal"),
		("Bloated", "Bloated"),
        ("Full", "Full"),
        ("Fluid", "Fluid"),
        ("Constipated", "Constipated")
	)

patient_appointment_type = (
		("Normal Visit", "Normal Visit"),
		("Emergency", "Emergency"),
        ("Exrternal Referrals", "Exrternal Referrals")
	)

appointment_status = (
		("Pending", "Pending"),
		("Open", "Open"),
        ("Closed", "Closed")
	)

class CustomUser(AbstractUser):
    mobile_no  = models.CharField(max_length=10)
    gender = models.CharField(max_length=20)
    address = models.TextField(null=True)
    user_type = models.CharField(default="Admin", choices=user_type_data, max_length=20)

    def __str__(self):
        return '{}'.format(self.username)


class PriceList(models.Model):
    price_list_name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return '{}'.format(self.price_list_name)


class ItemGroup(models.Model):
    group_name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return '{}'.format(self.group_name)


class Item(models.Model):
    item_code = models.CharField(primary_key=True, max_length=50)
    item_name = models.CharField(max_length=50)
    description = models.TextField()
    item_group = models.ForeignKey(ItemGroup, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.item_code)


class ItemPrice(models.Model):
    id = models.AutoField(primary_key=True)
    item_code = models.ForeignKey(Item, on_delete=models.CASCADE)
    price_list = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    price_list_rate = models.FloatField()


class Patient(models.Model):
    full_name = models.CharField(primary_key=True, max_length=50)
    email = models.EmailField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.full_name)
    

class InsuranceRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    insurance_company = models.CharField(max_length=50)
    covarage_plan = models.CharField(max_length=50)
    cardno = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return '{} - {}'.format(self.patient, self.insurance_company)


class Receptionist(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(primary_key=True, max_length=50)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to='media/img/receptionist', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}'.format(self.full_name)


class Nurse(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(primary_key=True, max_length=50)
    date_of_birth = models.DateField()
    profile_pic = models.ImageField(upload_to='media/img/nurse', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.full_name)


class MedicalDepartment(models.Model):
    department_name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.department_name)


class PractitionerSpeciality(models.Model):
    speciliaty_name = models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return '{}'.format(self.speciliaty_name)


class Practitioner(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(primary_key=True, max_length=50)
    date_of_birth = models.DateField()
    medical_department = models.ForeignKey(MedicalDepartment, on_delete=models.DO_NOTHING)
    speciality = models.ForeignKey(PractitionerSpeciality, on_delete=models.DO_NOTHING)
    consultation_item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField(upload_to='media/img/practitioner')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.full_name)

class SalesInvoice(models.Model):
    name = models.CharField(primary_key=True, max_length=50, blank=True)
    posting_date = models.DateField()
    posting_time = models.TimeField()
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.DO_NOTHING)
    department = models.ForeignKey(MedicalDepartment, on_delete=models.DO_NOTHING)
    reference_name = models.CharField(max_length=50)
    reference_number = models.CharField(max_length=50)
    item_code = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    amount = models.FloatField()
    created_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name = '{}-{}-{}-{}-{}'.format(
            "SI",
            get_abbr(self.patient),
            get_abbr(self.practitioner),
            get_date_str_combined(self.created_at),
            int(count_data(SalesInvoice)) + 1 
        )
        super(SalesInvoice, self).save(*args, **kwargs)
    
    def __str__(self):
        return "{}".format(self.name)
    

class PatientAppointment(models.Model):
    name = models.CharField(primary_key=True, max_length=50, blank=True)
    status = models.CharField(default="Pending", choices=appointment_status, max_length=50)
    patient =  models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=50)
    appointment_type = models.CharField(default="Normal Visit", choices=patient_appointment_type, max_length=50)
    medical_department = models.ForeignKey(MedicalDepartment, on_delete=models.DO_NOTHING)
    speciality = models.ForeignKey(PractitionerSpeciality, on_delete=models.DO_NOTHING)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.DO_NOTHING)
    is_cash_patient = models.BooleanField()
    insurance_subscription = models.ForeignKey(InsuranceRecord, on_delete=models.DO_NOTHING, blank=True, null=True)
    coverage_plan = models.CharField(max_length=50, blank=True, null=True)
    cardno = models.CharField(max_length=20, blank=True, null=True)
    insurance_company = models.CharField(max_length=50, blank=True, null=True)
    authorization_no = models.CharField(max_length=50, blank=True, null=True)
    invoice_no = models.CharField(max_length=50, blank=True, null=True)
    billing_item = models.CharField(max_length=50, blank=True, null=True)
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.name = '{}-{}-{}-{}-{}'.format(
            "PA",
            get_abbr(self.patient),
            get_abbr(self.practitioner),
            get_date_str_combined(self.created_at),
            int(count_data(PatientAppointment)) + 1 
        )
        super(PatientAppointment, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.name)


class VitalSign(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    appointment_no = models.ForeignKey(PatientAppointment, on_delete=models.DO_NOTHING)
    appointment_type = models.CharField(default="Normal Visit", choices=patient_appointment_type, max_length=50)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.DO_NOTHING)
    paid = models.BooleanField()
    body_templature = models.CharField(max_length=20)
    heart_rate = models.CharField(max_length=20)
    respiratory_rate = models.CharField(max_length=20)
    oxygen_saturation_spo2 = models.CharField(max_length=20)
    rbg = models.CharField(max_length=20)
    heart_rate = models.CharField(max_length=20)
    abdomen = models.CharField(default="Normal", choices=patient_abdomen_type, max_length=50)
    bp_systolic = models.CharField(max_length=20)
    bp_diastolic = models.CharField(max_length=20)
    bp = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    bmi = models.CharField(max_length=20)
    vital_signs_note = models.TextField()
    

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="media/img/services")
    department = models.ForeignKey(MedicalDepartment, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{}'.format(self.service_name)