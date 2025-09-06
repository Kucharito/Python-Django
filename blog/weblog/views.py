from django.shortcuts import render, get_object_or_404,redirect
from .models import Address, Userr, WorkRecord, Task, Client, Materials, MaterialsUsed, PlaceOfWork, Profession
from .forms import UserrForm, EmployeeLoginForm, UserrForm, WorkRecordForm, ClientForm, TaskForm, PlaceOfWorkForm, \
    AddressForm, ProfessionForm, MaterialsUsedForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import csv
from django.http import HttpResponse, JsonResponse
import os
import csv
from django.conf import settings
def index(request):

    return render(request, 'index.html')


def employee(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            try:
                user = Userr.objects.get(first_name=first_name, last_name=last_name, password_user=password,
                                         role_user='Z')
                return redirect('MenuZamestnanec')
            except Userr.DoesNotExist:
                error_message = "Nesprávne údaje"
        else:
            error_message = "Nesprávne údaje, skúste znovu."
    else:
        form = EmployeeLoginForm()
        error_message = None

    return render(request, 'employee.html', {'form': form, 'error_message': error_message})

def management(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            try:
                user = Userr.objects.get(first_name=first_name, last_name=last_name, password_user=password,
                                         role_user='V')
                return redirect('VeduciHlavneOkno')
            except Userr.DoesNotExist:
                error_message = "Nesprávne údaje."
        else:
            error_message = "Nesprávne údaje, skúste znovu."
    else:
        form = EmployeeLoginForm()
        error_message = None

    return render(request, 'management.html', {'form': form, 'error_message': error_message})

def zaznam(request):
    form = UserrForm()
    return render(request, 'zaznam.html', {'form': form})

def add_user(request):
    if request.method == 'POST':
        form = UserrForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User bol úspešne pridaný.')
            return redirect('zaznam')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')

    else:
        form = UserrForm()
    return render(request, 'zaznam.html', {'form': form})

def odstranit_user(request,user_id):
    user = Userr.objects.get(pk=user_id)
    user.delete()
    return redirect('VsetkyInfo')

def MenuZamestnanec(request):
    return render(request, 'MenuZamestnanec.html')



def add_work_record(request):
    if request.method == 'POST':
        form = WorkRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Záznam bol úspešne pridaný.')
            return redirect('add_work_record')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')

    else:
        form = WorkRecordForm()
    return render(request, 'AddRecord.html', {'form': form})

def DeadlinesEmployee(request):
    tasks = Task.objects.all()
    return render(request, 'DeadlinesEmployee.html', {'tasks': tasks})

def VeduciHlavneOkno(request):
    tasks = Task.objects.all()
    return render(request,'VeduciHlavneOkno.html',{'tasks': tasks})


def pridat_klienta(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Klient bol úspešne pridaný.')
            return redirect('pridat_klienta')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')
    else:
        form = ClientForm()
    return render(request, 'PridatKlienta.html', {'form': form})


def odstranit_klient(request,klient_id):
    klient = Client.objects.get(pk=klient_id)
    klient.delete()
    return redirect('VsetkyInfo')


def pridat_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Úloha bola úspešne pridaná.')
            return redirect('pridat_task')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')
    else:
        form = TaskForm()
    return render(request, 'PridatTask.html', {'form': form})



def odstranit_task(request, uloha_id):
    task = Task.objects.get(pk=uloha_id)
    task.delete()
    return redirect('VsetkyInfo')



def VsetkyInfo(request):
    zaznamy_userov = WorkRecord.objects.all()
    vsetky_ulohy = Task.objects.all()
    vsetci_klienti = Client.objects.all()
    vsetky_materialy=Materials.objects.all()
    pouzite_materialy=MaterialsUsed.objects.all()
    pracovne_miesta=PlaceOfWork.objects.all()
    vsetci_pouzivatelia=Userr.objects.all()
    vsetky_profesie=Profession.objects.all()
    return render(request, 'VsetkyInfo.html', {'zaznamy_userov': zaznamy_userov, 'vsetky_ulohy': vsetky_ulohy, 'vsetci_klienti': vsetci_klienti,'vsetky_materialy':vsetky_materialy,'pouzite_materialy':pouzite_materialy,'pracovne_miesta':pracovne_miesta,'vsetci_pouzivatelia':vsetci_pouzivatelia,'vsetky_profesie':vsetky_profesie})

def pridat_pracovisko(request):
    if request.method == 'POST':
        place_of_work_form = PlaceOfWorkForm(request.POST)
        if place_of_work_form.is_valid():
            place_of_work_form.save()
            messages.success(request, 'Pracovisko bolo úspešne pridané.')
            return redirect('pridat_pracovisko')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')

    else:
        place_of_work_form = PlaceOfWorkForm()
    return render(request, 'pridat_pracovisko.html', {'place_of_work_form': place_of_work_form})

def odstranit_workplace(request, workplace_id):
    pracovisko = PlaceOfWork.objects.get(pk=workplace_id)
    pracovisko.delete()
    return redirect('VsetkyInfo')

def pridat_adresu(request):
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address_form.save()
            messages.success(request, 'Adresa bola úspešne pridaná.')
            return redirect('pridat_adresu')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')

    else:
        address_form = AddressForm()
    return render(request, 'PridatAdresu.html', {'address_form': address_form})


def odstranit_material(request, material_id):
    material = Materials.objects.get(pk=material_id)
    material.delete()
    return redirect('VsetkyInfo')

def pridat_profesiu(request):
    if request.method == 'POST':
        profession_form = ProfessionForm(request.POST)
        if profession_form.is_valid():
            profession_form.save()
            messages.success(request, 'Profesia bola úspešne pridaná.')
            return redirect('pridat_profesiu')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')

    else:
        profession_form = ProfessionForm()
    return render(request, 'PridatProfesiu.html', {'profession_form': profession_form})

def odstranit_profesiu(request, profession_id):
    profession = Profession.objects.get(pk=profession_id)
    profession.delete()
    return redirect('VsetkyInfo')

def pouzite_materialy(request):
    if request.method == 'POST':
        materialsused_form = MaterialsUsedForm(request.POST)
        if materialsused_form.is_valid():
            materialsused_form.save()
            messages.success(request, 'Material bol pridaný ako použitý.')
            return redirect('pouzite_materialy')
        else:
            messages.error(request, 'Formulár nebol vyplnený správne.')
    else:
        materialsused_form = MaterialsUsedForm()
    return render(request, 'PouziteMaterialy.html', {'materialsused_form': materialsused_form})


def work_record(request):
    if request.method == 'POST':
        id_user = request.POST.get('id_user')
        user_work_records = WorkRecord.objects.filter(id_user=id_user)
        users = Userr.objects.all()
        return render(request, 'WorkRecords.html', {'user_work_records': user_work_records, 'users': users})
    else:
        users = Userr.objects.all()
        return render(request, 'WorkRecords.html', {'users': users})

def export_all_users_to_csv(request):
    users = Userr.objects.all()

    # Vytvorenie HTTP odpovede s CSV súborom
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_users.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Role', 'Skills',
                     'Profession (ID, Name)', 'Address (ID, Full Address)'])

    for user in users:
        writer.writerow([
            user.id,
            user.first_name,
            user.last_name,
            user.email,
            user.phone_number,
            user.get_role_user_display(),
            user.skills or "N/A",
            f"{user.id_profession.id}, {user.id_profession.profession_name}",
            f"{user.id_address.id}, {user.id_address.address_name} {user.id_address.address_number}, "
            f"{user.id_address.address_city}, {user.id_address.address_country}, {user.id_address.postal_code}"
        ])
    return response

def export_all_tasks_to_csv(request):
    tasks = Task.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="all_tasks.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Task Name', 'Description', 'Status', 'Creation Date', 'Completion Date',
                     'Comments', 'User (ID, Name)', 'Client (ID, Name)', 'Place of Work (ID, Name)'])

    for task in tasks:
        writer.writerow([
            task.id,
            task.task_name,
            task.task_description or "N/A",
            task.actual_status or "N/A",
            task.date_of_creation,
            task.date_of_completion,
            task.comments or "N/A",
            f"{task.id_user.id}, {task.id_user.first_name} {task.id_user.last_name}",
            f"{task.id_client.id}, {task.id_client.first_name} {task.id_client.last_name}",
            f"{task.id_place_of_work.id}, {task.id_place_of_work.construction_name}"
        ])
    return response

def export_all_tables_to_csv(request):
    models = [
        (Userr, 'users.csv', ['ID', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Role', 'Skills']),
        (Task, 'tasks.csv', ['ID', 'Task Name', 'Description', 'Status', 'Creation Date', 'Completion Date', 'Comments',
                             'User (ID, Name)', 'Client (ID, Name)', 'Place of Work (ID, Name)']),
        (Client, 'clients.csv', ['ID', 'First Name', 'Last Name', 'Email', 'Phone Number', 'Company Name']),
        (Materials, 'materials.csv', ['ID', 'Material Name', 'Description', 'Quantity']),
        (MaterialsUsed, 'materials_used.csv', ['ID', 'Quantity Used', 'Work Record ID', 'Material ID']),
        (PlaceOfWork, 'places_of_work.csv', ['ID', 'Construction Name', 'Address (ID, Full Address)']),
        (Profession, 'professions.csv', ['ID', 'Profession Name', 'Required Skills', 'Certifications']),
        (WorkRecord, 'work_records.csv', ['ID', 'Description', 'Date', 'User (ID, Name)', 'Task (ID, Name)', 'Place of Work (ID, Name)']),
    ]

    export_dir = os.path.join(settings.BASE_DIR, 'exports')
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    for model, file_name, headers in models:
        file_path = os.path.join(export_dir, file_name)
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)

            for obj in model.objects.all():
                if model == Userr:
                    writer.writerow([
                        obj.id,
                        obj.first_name,
                        obj.last_name,
                        obj.email,
                        obj.phone_number,
                        obj.get_role_user_display(),
                        obj.skills or "N/A"
                    ])
                elif model == Task:
                    writer.writerow([
                        obj.id,
                        obj.task_name,
                        obj.task_description or "N/A",
                        obj.actual_status or "N/A",
                        obj.date_of_creation,
                        obj.date_of_completion,
                        obj.comments or "N/A",
                        f"{obj.id_user.id}, {obj.id_user.first_name} {obj.id_user.last_name}",
                        f"{obj.id_client.id}, {obj.id_client.first_name} {obj.id_client.last_name}",
                        f"{obj.id_place_of_work.id}, {obj.id_place_of_work.construction_name}"
                    ])
                elif model == Client:
                    writer.writerow([
                        obj.id,
                        obj.first_name or "N/A",
                        obj.last_name or "N/A",
                        obj.email,
                        obj.phone_number,
                        obj.company_name or "N/A"
                    ])
                elif model == Materials:
                    writer.writerow([
                        obj.id,
                        obj.material_name,
                        obj.material_description,
                        obj.material_quantity
                    ])
                elif model == MaterialsUsed:
                    writer.writerow([
                        obj.id,
                        obj.quantity_used,
                        f"{obj.id_work_record.id}",
                        f"{obj.id_materials.id}"
                    ])
                elif model == PlaceOfWork:
                    writer.writerow([
                        obj.id,
                        obj.construction_name,
                        f"{obj.id_address.id}, {obj.id_address.address_name} {obj.id_address.address_number}, "
                        f"{obj.id_address.address_city}, {obj.id_address.address_country}, {obj.id_address.postal_code}"
                    ])
                elif model == Profession:
                    writer.writerow([
                        obj.id,
                        obj.profession_name,
                        obj.required_skills,
                        obj.certifications
                    ])
                elif model == WorkRecord:
                    writer.writerow([
                        obj.id,
                        obj.description or "N/A",
                        obj.date_work_record,
                        f"{obj.id_user.id}, {obj.id_user.first_name} {obj.id_user.last_name}",
                        f"{obj.id_task.id}, {obj.id_task.task_name}" if obj.id_task else "N/A",
                        f"{obj.id_place_of_work.id}, {obj.id_place_of_work.construction_name}"
                    ])

    return JsonResponse({'message': 'All tables have been exported to CSV files', 'directory': export_dir})
