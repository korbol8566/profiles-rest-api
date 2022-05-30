from django.db                      import models
from django.contrib.auth.models     import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User profiles"""
    
    def create_user(self,email, name, password=None):
        """Create a new User profile"""
        if not email:
            raise ValueError("Please provide an email address")
        
        email=self.normalize_email(email)
        user=self.create_user(email=email,name=name)
        
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self, email, name, password):
        """Create a new superuser with given details"""
        user=self.create_user(email, name, password)
        
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)
        
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    DB model for users in the system
    """
    
    email       = models.EmailField(max_length=255, unique=True)
    name        = models.CharField(max_length=255)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)

    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name']
    
    def get_full_name(self):
        """retrieve full name of user """
        return self.name
    
    def get_short_name(self):
        """retrieve short name of user """
        return self.name
    
    def __str__(self):
        """returns string representation of our user """
        return self.email