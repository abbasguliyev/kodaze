from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from .managers import CustomUserManager
from main.image_validator import file_size

# Create your models here.
class User(AbstractUser):
    HOURLY = "SAATLIQ"
    WEEKLY = "HƏFTƏLİK"
    MONTHLY = "AYLIQ"

    SALARY_CALCULATION_STYLE = [
        (HOURLY, "SAATLIQ"),
        (WEEKLY, "HƏFTƏLİK"),
        (MONTHLY, "AYLIQ")
    ]

    MALE = "Kişi"
    FERMALE = "Qadın"

    GENDER_CHOICES = [
        (MALE, "Kişi"),
        (FERMALE, "Qadın")
    ]

    date_of_birth= models.DateField(null=True, blank=True)
    job_start_date= models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now = True)
    tel1=models.CharField(max_length=200)
    tel2=models.CharField(max_length=200, null=True, blank=True)
    id_card_image=models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    company=models.ForeignKey("company.Company", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    office=models.ForeignKey("company.Office", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    department=models.ForeignKey("company.Department", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    position = models.ForeignKey("company.Position", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    electronic_signature = models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True,  validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    gender = models.CharField(
        max_length=150,
        choices=GENDER_CHOICES,
        default=None,
        null=True,
        blank=True 
    )
    salary_calculation_style = models.CharField(
        max_length=150,
        choices=SALARY_CALCULATION_STYLE,
        default=MONTHLY,
        null=True,
        blank=True
    )
    
    hourly_salary = models.FloatField(default=0)
    weekly_salary = models.FloatField(default=0)
    monthly_salary = models.FloatField(default=0)

    salary = models.FloatField(default=0, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ("-pk",)  

    def __str__(self):
        return f"{self.username}"

class Supervizor(models.Model):
    supervizor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="supervizor")
    users = models.ManyToManyField(User, related_name="supervizor_users")

class WorkExperiences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_experiences")
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    note = models.TextField(null=True, blank=True)
    start_job_date = models.DateField(default=None, null=True, blank=True)
    end_job_date = models.DateField(default=None, null=True, blank=True)
    termination_reason = models.CharField(max_length=500, null=True, blank=True)

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=200)
    knowledge_level = models.CharField(max_length=200)

class Languages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="languages")
    title = models.CharField(max_length=200)
    knowledge_level = models.CharField(max_length=200)

class Customer(models.Model):
    MALE = "Kişi"
    FERMALE = "Qadın"

    GENDER_CHOICES = [
        (MALE, "Kişi"),
        (FERMALE, "Qadın")
    ]

    PERSONAL = "ŞƏXS"
    ORGANIZIATION = "KORPORATİV"

    CUSTOMER_TYPE_CHOICES = [
        (PERSONAL, "ŞƏXS"),
        (ORGANIZIATION, "KORPORATİV")
    ]
    company_name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth= models.DateField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now = True)
    tel1 = models.CharField(max_length=50)
    tel2 = models.CharField(max_length=50, null=True, blank=True)
    tel3 = models.CharField(max_length=50, null=True, blank=True)
    tel4 = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField()
    id_card_image=models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    gender = models.CharField(
        max_length=150,
        choices=GENDER_CHOICES,
        default=None,
        null=True,
        blank=True 
    )
    customer_type = models.CharField(
        max_length=150,
        choices=CUSTOMER_TYPE_CHOICES,
        default=None,
        null=True
    )
    note = models.TextField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-pk",)  

    def __str__(self):
        return f"{self.company_name} {self.first_name} {self.last_name}"


class Address(models.Model):
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250, null=True, blank=True)
    district = models.CharField(max_length=250, null=True, )
    street = models.CharField(max_length=250, null=True)
    postal_code = models.CharField(max_length=300, null=True, blank=True)

class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="addresses")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="users")

class CustomerAddress(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name="addresses")
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="customer")