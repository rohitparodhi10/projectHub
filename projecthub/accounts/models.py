from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        # Create a superuser without the create_user method
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True, blank=None, null=None)
    user_image=models.ImageField(upload_to='user_image', null=True, blank=True)
    login_count=models.PositiveIntegerField(default=0)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['password']
    
    objects=CustomUserManager()
