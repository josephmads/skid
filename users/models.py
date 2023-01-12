from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify

User=get_user_model()

# Create your models here.

class Material(models.Model):
    """Model representing the materials a user works with."""
    material = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.material

class Skill(models.Model):
    """Model representing the skills a user has."""
    skill = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill

class WorkType(models.Model):
    """Model representing the type of work a user can do."""
    work_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.work_type

class Profile(models.Model):    
    """Model representing a users personal information."""
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100, blank=True)
    business_name = models.CharField(max_length=100, blank=True)
    email_public = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state_province = models.CharField('State or Province', max_length=100, blank=True)
    zip_code = models.CharField('Zip or Postal Code', max_length=10, blank=True)
    country = models.CharField(max_length=56, blank=True)
    about = models.TextField(blank=True)

    skills = models.ManyToManyField(to=Skill, related_name='users', blank=True)
    materials = models.ManyToManyField(to=Material, related_name='users', blank=True)
    type_of_work = models.ManyToManyField(
        to=WorkType,
        related_name='users', 
        blank=True,
        help_text='eg: Prototype, Production, Made to Order, etc.')

    def get_absolute_url(self):
        """Returns URL to access a particular user instance."""
        return reverse('directory:user_detail', args=[str(self.username)])

    
class Idea(models.Model):
    """Model representing an Idea that a user shares with other others."""
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='idea')
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=140, default='', null=True, blank=True, unique=True)
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    skills = models.ManyToManyField(
        to=Skill, 
        related_name='idea', 
        blank=True,
        help_text='Type of skills needed for this Idea.')

    materials = models.ManyToManyField(
        to=Material, 
        related_name='idea', 
        blank=True,
        help_text='Type of materials needed for this Idea.')

    type_of_work = models.ManyToManyField(
        to=WorkType,
        related_name='idea', 
        blank=True,
        help_text='How many do you need made? eg: one = prototype, many = production, etc.')

    IDEA_STATUS = (
        ('d', 'Draft'),
        ('p', 'Publish'),
    )

    status = models.CharField(
        max_length=1,
        choices=IDEA_STATUS,
        blank=True,
        default='d',
    )

    def __str__(self):
        """String for representing the Idea."""
        return f'{self.title} - by, {self.username}'

    def get_absolute_url(self):
        return reverse('directory:idea_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

