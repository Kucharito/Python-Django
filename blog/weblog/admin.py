from django.contrib import admin

# Register your models here.
from .models import Address,Client,Materials,MaterialsUsed,PlaceOfWork,Profession,Task,Userr,WorkRecord,WorkRecordHistory
admin.site.register(Address)
admin.site.register(Client)
admin.site.register(Materials)
admin.site.register(MaterialsUsed)
admin.site.register(PlaceOfWork)
admin.site.register(Profession)
admin.site.register(Task)
admin.site.register(Userr)
admin.site.register(WorkRecord)
admin.site.register(WorkRecordHistory)
