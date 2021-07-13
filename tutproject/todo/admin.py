from django.contrib import admin
from .models import taskModels,subTaskModels,groupModels,testFieldsMoels
# Register your models here.


admin.site.register(taskModels)
admin.site.register(subTaskModels)
admin.site.register(groupModels)
admin.site.register(testFieldsMoels)

