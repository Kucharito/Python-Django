from django import forms
from .models import Userr, WorkRecord, Client, Task, Address, PlaceOfWork, Profession, MaterialsUsed


class UserrForm(forms.ModelForm):
    class Meta:
        model = Userr
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'skills', 'password_user', 'id_profession', 'id_address', 'role_user']

class EmployeeLoginForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class WorkRecordForm(forms.ModelForm):
    class Meta:
        model = WorkRecord
        fields = ['description', 'date_work_record', 'id_user', 'id_task', 'id_place_of_work']
        widgets = {
            'date_work_record': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'company_name']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'actual_status', 'date_of_creation', 'date_of_completion', 'comments', 'id_user', 'id_client','id_place_of_work']
        widgets = {
            'date_of_creation': forms.DateInput(attrs={'type': 'date'}),
            'date_of_completion': forms.DateInput(attrs={'type': 'date'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_name', 'address_number', 'address_city', 'address_country', 'postal_code']


class PlaceOfWorkForm(forms.ModelForm):
    class Meta:
        model = PlaceOfWork
        fields = ['construction_name', 'id_address']

class ProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        fields = ['profession_name', 'required_skills','certifications']

class MaterialsUsedForm(forms.ModelForm):
    class Meta:
        model = MaterialsUsed
        fields = ['quantity_used', 'id_work_record','id_materials']