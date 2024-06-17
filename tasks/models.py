from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _  #ugettext_lazy 
# Create your models here.





class Tasks(models.Model):
    title= models.CharField(max_length=150)
    description = models.TextField()   
    time_estimation = models.IntegerField() # store time in seconds 
    created_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=50)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', verbose_name=_("Assignee"), null=True, blank=True)
    assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned_by', verbose_name=_("Assigned By"), null=True, blank=True)
    is_deleted = models.BooleanField( default = False)
 
 