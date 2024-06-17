from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _  #ugettext_lazy 
from .managers import UserManager
# Create your models here.




class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first_name"), max_length=50)
    second_name = models.CharField(_("second_name"), max_length=50)
    is_activated = models.BooleanField(_(""), default = False)
    is_deleted = models.BooleanField(_(""), default = False)
    role = models.CharField(_(""), max_length=50)
    job_title = models.CharField(_("job_title"), max_length=50)  
    description = models.TextField(_("")) 
    email = models.EmailField(_(""), max_length=254, unique = True)
    created_at = models.DateTimeField(_(""), auto_now_add=True)
    updated_at = models.DateTimeField(_(""), auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
class UserToken(models.Model):
    token = models.UUIDField(_(""), unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_(""), auto_now_add=True)
    
    
    
    
    


