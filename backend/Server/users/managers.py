from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager
from django.utils.crypto import get_random_string


class UserManager(BaseUserManager):
    # Method to create user with provided credentials
    def create_user(self, username, email , id=None, password=None): 
        email = email.lower()
        user_id = get_random_string(50)
        user = self.model( 
            username = username,
            email = email,
            id = user_id
        ) 
        user.set_password(password) 
        user.save(using = self._db) 
        return user 

    # Method to create superuser with provided credentials
    def create_superuser(self, username, email, id=None, password=None):
        user_id = get_random_string(50)
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            id = user_id,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    