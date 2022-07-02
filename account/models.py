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
    tel2=models.CharField(max_length=200, null=True)
    sv_image=models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    company=models.ForeignKey("company.Company", on_delete=models.SET_NULL, related_name="users", null=True)
    office=models.ForeignKey("company.Office", on_delete=models.SET_NULL, related_name="users", null=True)
    department=models.ForeignKey("company.Department", on_delete=models.SET_NULL, related_name="users", null=True)
    position = models.ForeignKey("company.Position", on_delete=models.SET_NULL, related_name="users", null=True)
    electronic_signature = models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
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
        ordering = ("pk",)  

    def __str__(self):
        return f"{self.username}"