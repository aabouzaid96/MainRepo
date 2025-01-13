from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.http import JsonResponse


class CustomUserManager(BaseUserManager):
    def create_user(self, email, firstName, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, firstName=firstName)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstName, password=None):
        user = self.create_user(email, firstName, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=150)
    password = models.CharField(max_length=128, null=True, blank=True)  # Temporarily allow null

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName']

    def __str__(self):
        return self.email


def sample_view(request):
    return JsonResponse({"message": "Hello from Main Repo, Karem Changes"})
