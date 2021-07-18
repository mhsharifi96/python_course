from django.contrib import admin
from .models import taskModels,subTaskModels,groupModels,testFieldsMoels,person,groupPerson
# Register your models here.

class SystemAdmin(admin.ModelAdmin):
    filter_horizontal = ('person',) 


admin.site.register(taskModels)
admin.site.register(subTaskModels)
admin.site.register(groupModels)
admin.site.register(groupPerson,SystemAdmin)
admin.site.register(testFieldsMoels)
admin.site.register(person)

