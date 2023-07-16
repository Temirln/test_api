from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_user(self,username,email,password,**other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)

        user = self.model(email = email,username = username,**other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,username,email,password,**other_fields):
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault("is_admin",True)
        other_fields.setdefault("is_superuser",True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be Staff")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")
        if other_fields.get("is_admin") is not True:
            raise ValueError("Superuser must be admin")
        
        return self.create_user(username,email,password,**other_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100,unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    

    def __str__(self) -> str:
        return self.title


class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Order number:{self.pk}-{self.user}"

    
if __name__ == "__main__":
    f1driver = CustomUser.objects.filter()
    print(f1driver)