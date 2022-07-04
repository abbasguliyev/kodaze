from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from .managers import CustomUserManager
from main.image_validator import file_size


class Address(models.Model):
    country = models.CharField(max_length=250)
    city = models.CharField(max_length=250, null=True, blank=True)
    district = models.CharField(max_length=250, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    postal_code = models.CharField(max_length=300, null=True, blank=True)

    class Meta:
        ordering = ("-pk",)

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

    FREELANCER = "Xidməti müqavilə"
    EMPLOYEE = "Əmək müqaviləsi"
    INTERN = "Təcrübəçi"

    EMPLOYEE_TYPE_CHOICES = [
        (FREELANCER, "Xidməti müqavilə"),
        (EMPLOYEE, "Əmək müqaviləsi"),
        (INTERN, "Təcrübəçi")
    ]

    MARRIED = "Evli"
    SINGLE = "Subay"

    MARTIAL_STATUS_CHOICES = [
        (MARRIED, "Evli"),
        (SINGLE, "Subay")
    ]

    date_of_birth= models.DateField(null=True, blank=True)
    job_start_date= models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now = True)

    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    
    tel1=models.CharField(max_length=200)
    tel2=models.CharField(max_length=200, null=True, blank=True)
    work_phone1 = models.CharField(max_length=200, null=True, blank=True)
    work_phone2 = models.CharField(max_length=200, null=True, blank=True)
    work_email = models.EmailField(max_length=200, null=True, blank=True)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    
    profile_image = models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    id_card_image = models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    passport_image = models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    driving_license_image = models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    electronic_signature = models.ImageField(upload_to="media/account/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    
    company = models.ForeignKey("company.Company", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    office = models.ForeignKey("company.Office", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    department = models.ForeignKey("company.Department", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)
    position = models.ForeignKey("company.Position", on_delete=models.SET_NULL, related_name="users", null=True, blank=True)

    family_composition = models.PositiveIntegerField(default=1, null=True, blank=True)
    speaking_language = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(
        max_length=150,
        choices=GENDER_CHOICES,
        default=None,
        null=True,
        blank=True 
    )
    martial_status = models.CharField(
        max_length=150,
        choices=MARTIAL_STATUS_CHOICES,
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
    employee_type = models.CharField(
        max_length=150,
        choices=EMPLOYEE_TYPE_CHOICES,
        default=EMPLOYEE,
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

    class Meta:
        ordering = ("-pk",)

class WorkExperiences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_experiences")
    title = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    note = models.TextField(null=True, blank=True)
    start_job_date = models.DateField(default=None, null=True, blank=True)
    end_job_date = models.DateField(default=None, null=True, blank=True)
    termination_reason = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ("pk",)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=200)
    knowledge_level = models.CharField(max_length=200)

    class Meta:
        ordering = ("pk",)

class Language(models.Model):
    language = models.CharField(max_length=300)
    
    class Meta:
        ordering = ("pk",)

    def __str__(self) -> str:
        return self.language

class UserEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="educations")
    high_school = models.CharField(max_length=500, null=True, blank=True)
    college = models.CharField(max_length=500, null=True, blank=True)
    university = models.CharField(max_length=500, null=True, blank=True)
    diploma = models.ImageField(upload_to="media/account/education/%Y/%m/%d/", null=True, blank=True, validators=[file_size, FileExtensionValidator(['png', 'jpeg', 'jpg'])])

    class Meta:
        ordering = ("pk",)


class UserLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="languages")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="users")
    knowledge_level = models.CharField(max_length=200, null=True, blank=True)
    speeking = models.BooleanField(default=False, blank=True)
    listening = models.BooleanField(default=False, blank=True)
    reading = models.BooleanField(default=False, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("pk",)

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
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="customers")
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
        if self.company_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.company_name}"