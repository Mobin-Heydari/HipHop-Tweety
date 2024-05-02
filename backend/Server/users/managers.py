from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import get_random_string
from profiles.models import UserProfile


class UserManager(BaseUserManager):
    # Method to create user with provided credentials
    def create_user(self, username, email , password=None):
        
        email = email.lower()
        
        user = self.model( 
            username = username,
            email = email,
        )
        
        user.set_password(password) 
        
        user.save(using = self._db)
        
        user_profile = UserProfile.objects.create(
            user = user
        )
        
        user_profile.save() 
        
        return user 

    # Method to create superuser with provided credentials
    def create_superuser(self, username, email, password=None):
        
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        
        user.is_admin = True
        
        user.is_superuser = True
        
        user.save(using=self._db)
        
        user_profile = UserProfile.objects.create(
            user = user
        )
        
        user_profile.save()
        
        return user
    