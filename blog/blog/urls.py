"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('employee/', views.employee, name='employee'),
    path('management/', views.management, name='management'),
    path('MenuZamestnanec/', views.MenuZamestnanec, name='MenuZamestnanec'),
    path('zaznam/', views.zaznam, name='zaznam'),
    path('zaznam/add_user/', views.add_user, name='add_user'),
    path('add_work_record/', views.add_work_record, name='add_work_record'),
    path('DeadlinesEmployee/', views.DeadlinesEmployee, name='DeadlinesEmployee'),
    path('VeduciHlavneOkno/', views.VeduciHlavneOkno, name='VeduciHlavneOkno'),
    path('pridat_klienta/', views.pridat_klienta, name='pridat_klienta'),
    path('pridat_task/', views.pridat_task, name='pridat_task'),
    path('VsetkyInfo/', views.VsetkyInfo, name='VsetkyInfo'),
    path('pridat_pracovisko/', views.pridat_pracovisko, name='pridat_pracovisko'),
    path('pridat_adresu/',views.pridat_adresu, name='pridat_adresu'),
    path('pridat_profesiu/',views.pridat_profesiu, name='pridat_profesiu'),
    path('pouzite_materialy/',views.pouzite_materialy, name='pouzite_materialy'),
    path('odstranit_task/<int:uloha_id>', views.odstranit_task, name='odstranit_task'),
    path('odstranit_klient/<int:klient_id>', views.odstranit_klient, name='odstranit_klient'),
    path('odstranit_material/<int:material_id>', views.odstranit_material, name='odstranit_material'),
    path('odstranit_workplace/<int:workplace_id>', views.odstranit_workplace, name='odstranit_workplace'),
    path('odstranit_user/<int:user_id>', views.odstranit_user, name='odstranit_user'),
    path('odstranit_profesiu/<int:profession_id>', views.odstranit_profesiu, name='odstranit_profesiu'),
    path('work_record/',views.work_record,name='work_record'),
    path('export_all_users/', views.export_all_users_to_csv, name='export_all_users_to_csv'),
    path('export_all_tasks/', views.export_all_tasks_to_csv, name='export_all_tasks_to_csv'),
    path('export_all_tables/', views.export_all_tables_to_csv, name='export_all_tables')

]
