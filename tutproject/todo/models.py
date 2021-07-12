from django.db import models
from tutproject.constants import  PORITY_TASK,STATUS_TASK,TYPE_TASK
# Create your models here.

# Model field reference
# https://docs.djangoproject.com/en/3.2/ref/models/fields/
# Making queries
# https://docs.djangoproject.com/en/3.2/topics/db/queries/

class taskModels(models.Model):
    
    # user
    # title
    title = models.CharField(max_length=250)
    # description
    description = models.TextField()
    # pority 1
    pority = models.IntegerField(choices=PORITY_TASK,default=4)
    # status
    status = models.CharField(max_length=10,choices=STATUS_TASK,default="enable")
    # type ? reminder or task
    type_task = models.CharField(max_length=10,choices=TYPE_TASK,default="task")
    # expire_date
    expire_date = models.DateTimeField(blank=True,null=True)
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at
    updated_at = models.DateTimeField(auto_now=True)
    # expire_date = models.datetime




class subTaskModels(models.Model):
    pass
    # task
    # title
    # description
    # pority
    # status
    # expire_date


class groupModels(models.Model):
    pass 
    # name
    # status
    # expire_date
    # created_at
    # updated_at


class group_taskModels(models.Model):
    pass
    # group
    # task
    # created_at
    # updated_at




class taskperiodModel(models.Model  ):
    pass 
    # task
    # startdate
    # end date
    # period time
    # status
    # created_at
    # updated_at


