from django.db import models
from django.contrib.auth.models import User

from tutproject.constants import  PORITY_TASK,STATUS_TASK,TYPE_TASK
# Create your models here.

# Model field reference
# https://docs.djangoproject.com/en/3.2/ref/models/fields/
# Making queries
# https://docs.djangoproject.com/en/3.2/topics/db/queries/

class taskModels(models.Model):
    
    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.title
    




class subTaskModels(models.Model):
    # task
    task = models.ForeignKey(taskModels, on_delete=models.CASCADE)
    # title
    title = models.CharField(max_length=50)
    # description
    description = models.TextField()
    # pority
    pority = models.IntegerField(choices=PORITY_TASK,default=4)
    # status
    status = models.CharField(max_length=10,choices=STATUS_TASK,default="enable")
    # expire_date
    expire_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title



class groupModels(models.Model):
   
    # name
    name = models.CharField(max_length=50)
    # status
    status = models.CharField(max_length=10,choices=STATUS_TASK,default="enable")
    # expire_date
    expire_date = models.DateTimeField(blank=True,null=True)
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class group_taskModels(models.Model):
    # group
    group = models.ForeignKey(groupModels, on_delete=models.CASCADE)
    # task
    task = models.ForeignKey(taskModels, on_delete=models.CASCADE)
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at
    updated_at = models.DateTimeField(auto_now=True)




class taskperiodModel(models.Model  ):
    pass 
    # task
    # startdate
    # end date
    # period time
    # status
    # created_at
    # updated_at





class testFieldsMoels(models.Model):
    
    name = models.CharField(max_length=500,db_column='nameTest')
    code  = models.IntegerField(db_column='codeTest',db_index=True)
    constant  = models.CharField(max_length=500,db_column='constantTest',editable=False,default='constant field')
    error_messages  = models.CharField(max_length=500,error_messages={'blank': 'نکن این کار رو با ما', 'null': 'چشم'})
    help_text = models.CharField(max_length=500,help_text="این متن برای کمک به توفقط والا")
    help_text = models.CharField(max_length=500,verbose_name="توضیح اضافی")
    dateFeild = models.DateField(blank=True,null=True)
    DateTimeField = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField()

    # unique ,primary_key

    # show error on error_message 
    #  run python manage.py shell 
    # import todo.models from testFieldsMoels 
    # testFieldsMoels().full_clean()
    #ref : https://stackoverflow.com/questions/4798322/how-do-i-use-error-messages-on-models-in-django

    def __str__(self):
        return self.name




# ManyToManyField
# OneToOne
