from __future__ import unicode_literals
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.
class  Users(AbstractUser):
    status=((1,"Teacher"),(2,"Student"))
    Type=models.IntegerField(choices=status,default=2,blank=False , help_text='1 for Teacher 2 for student')
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    Age=models.IntegerField(default=0)


    class Meta :
            verbose_name_plural = "Users"


    @property
    def token(self):
      return self.generate_jwt_token()

    def generate_jwt_token(self):
      dt = datetime.now() + timedelta(days=1)
      print("HI")
      token = jwt.encode(
        {
          'user': str(self),
          'type': self.Type,
          'exp': int(datetime.timestamp(dt))
        }, settings.SECRET_KEY, algorithm='HS256'
      )
      return token.decode('utf-8')

class Result(models.Model):
    student=models.ForeignKey(Users,on_delete=models.CASCADE,limit_choices_to={'Type':2})
    English = models.IntegerField(default=0)
    Maths=models.IntegerField(default=0,verbose_name="Maths")
    History=models.IntegerField(default=0)
    def __str__(self):
        return str(self.student)


