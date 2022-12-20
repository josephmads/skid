from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Skill(models.Model):
    """Model representing the skills a user has."""
    skill = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill

class Material(models.Model):
    """Model representing the materials a user works with."""
    material = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.material

class WorkType(models.Model):
    """Model representing the type of work a user can do."""
    work_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.work_type

class SkidUserDetail(models.Model):    
    """Model representing a users personal information."""
    username = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=140, default='', null=True, blank=True, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    business_name = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state_province = models.CharField('state or province', max_length=100, blank=True)
    zip_code = models.CharField('zip or postal code', max_length=10, blank=True)
    country = models.CharField(max_length=56, blank=True)

    skills = models.ManyToManyField(to=Skill, blank=True)
    materials = models.ManyToManyField(to=Material, blank=True)
    type_of_work = models.ManyToManyField(
        to=WorkType, 
        blank=True,
        help_text='eg: Prototype, Production, Made to Order, etc.')

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     """Returns URL to access a particular user instance."""
    #     return reverse('directory:user_detail', kwargs={'slug': self.slug})
        
    # def save(self, *args, **kwargs):
    #     value = self.username
    #     self.slug = slugify(value, allow_unicode=True)
    #     super().save(*args, **kwargs)
    

