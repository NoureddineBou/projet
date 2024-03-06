from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import datetime
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class user(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'phone_number' , 'email' , 'password']

    def __str__(self):
        return self.username


class SearchForm(models.Model):
    search_query = models.CharField(max_length=255)
    search_filters = models.CharField(max_length=255)

class Offerm(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    author = models.ForeignKey(user, on_delete=models.CASCADE)





class OfferCategory(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()

class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(OfferCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class OfferImage(models.Model):
    image_file = models.ImageField(upload_to='offer_images/')
    caption = models.CharField(max_length=255)

class Booking(models.Model):
    client = models.ForeignKey(user, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offerm, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)





class HomePage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_offers = models.ManyToManyField(Offer)