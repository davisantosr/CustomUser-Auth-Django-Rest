from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
  def create_user(self, username, email, password=None):
    if username is None:
      raise TypeError('Compo usuário é obrigatório')
    if email is None:
      raise TypeError('Campo email é obrigátório')

    user = self.model(username=username, email=self.normalize_email(email))
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, username, email, password=None):
    if password is None:
      raise TypeError('Password can not be empty')
    if email is None:
      raise TypeError('Email is necessary')
  
    user = self.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    return user

class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField(max_length=255, unique=True, db_index=True)
  email = models.EmailField(max_length=255, unique=True, db_index=True)
  telefone = models.CharField(max_length=13)
  cpf = models.IntegerField(max_length=13)
  is_verified = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  objects = UserManager()

  def __str__(self):
    return self.email

  def tokens(self):
    return ''

  


