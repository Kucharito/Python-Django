from django.db import models
from django.conf import settings
import os

class Address(models.Model):
    address_name = models.CharField(max_length=50)
    address_number = models.IntegerField()
    address_city = models.CharField(max_length=40)
    address_country = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=5)

    def __str__(self):
        return self.address_name+' '+str(self.address_number)+', '+str(self.address_city)+', '+str(self.address_country)

class Client(models.Model):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=13)
    company_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.company_name+', '+self.first_name+' '+self.last_name

class Materials(models.Model):
    material_name = models.CharField(max_length=50)
    material_description = models.CharField(max_length=255)
    material_quantity = models.IntegerField()

    def __str__(self):
        return self.material_name

class MaterialsUsed(models.Model):
    quantity_used = models.IntegerField()
    id_work_record = models.ForeignKey('WorkRecord', on_delete=models.CASCADE)
    id_materials = models.ForeignKey(Materials, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_materials) + ' ' +str(+self.quantity_used)+"ks " + ', ' + str(self.id_work_record)


class PlaceOfWork(models.Model):
    construction_name = models.CharField(max_length=60)
    id_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.construction_name+', '+str(self.id_address)

class Profession(models.Model):
    profession_name = models.CharField(max_length=40)
    required_skills = models.CharField(max_length=300)
    certifications = models.CharField(max_length=300)

    def __str__(self):
        return self.profession_name

class Task(models.Model):
    task_name = models.CharField(max_length=40)
    task_description = models.CharField(max_length=200, blank=True, null=True)
    actual_status = models.CharField(max_length=100, blank=True, null=True)
    date_of_creation = models.DateField()
    date_of_completion = models.DateField()
    comments = models.CharField(max_length=100, blank=True, null=True)
    id_user = models.ForeignKey('Userr', on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_place_of_work = models.ForeignKey(PlaceOfWork, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.task_name


class Userr(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=13)
    skills = models.CharField(max_length=500, blank=True, null=True)
    password_user = models.CharField(max_length=30)

    id_profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    id_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    Veduci ='V'
    Zamestanec='Z'
    Moznosti_usera=[
        (Veduci,'Veduci'),
        (Zamestanec,'Zamestnanec'),
    ]
    role_user = models.CharField(max_length=20,choices=Moznosti_usera)


    def __str__(self):
        return self.role_user+', '+self.first_name+' '+self.last_name+', '+self.phone_number


class WorkRecord(models.Model):
    description = models.CharField(max_length=500, blank=True, null=True)
    date_work_record = models.DateField(blank=True, null=True)
    id_user = models.ForeignKey(Userr, on_delete=models.CASCADE)
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    id_place_of_work = models.ForeignKey(PlaceOfWork, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description}, {self.date_work_record.strftime('%Y-%m-%d')},{self.id_user}"

class WorkRecordHistory(models.Model):
    modified_at = models.DateField()
    old_description = models.CharField(max_length=2000)
    new_description = models.CharField(max_length=2000)
    id_work_record = models.ForeignKey(WorkRecord, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Userr, on_delete=models.CASCADE)
