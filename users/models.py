from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User=get_user_model()

# Create your models here.

class Material(models.Model):
    """Model representing the materials a user works with."""
    material = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.material

    def save(self, *args, **kwargs):
        self.material = self.material.lower()
        return super(Material, self).save(*args, **kwargs)

class Skill(models.Model):
    """Model representing the skills a user has."""
    skill = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill

    def save(self, *args, **kwargs):
        self.skill = self.skill.lower()
        return super(Skill, self).save(*args, **kwargs)

class WorkType(models.Model):
    """Model representing the type of work a user can do."""
    work_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.work_type

    def save(self, *args, **kwargs):
        self.work_type = self.work_type.lower()
        return super(WorkType, self).save(*args, **kwargs)

class Profile(models.Model):    
    """Model representing a users personal information."""
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100, blank=True)
    email_public = models.EmailField(
        'Public Email',
        blank=True,
        null=True,
        max_length=100, 
        help_text='This email address will be displayed on your public SKID profile.'
        )
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state_province = models.CharField('State or Province', max_length=100, blank=True)
    zip_code = models.CharField('Zip or Postal Code', max_length=10, blank=True)
    country = models.CharField(max_length=56, blank=True)
    about = models.TextField(blank=True)

    skills = models.ManyToManyField(to=Skill, related_name='profile', blank=True)
    materials = models.ManyToManyField(to=Material, related_name='profile', blank=True)
    type_of_work = models.ManyToManyField(
        to=WorkType,
        related_name='profile', 
        blank=True,
        help_text='eg: Prototype, Production, Made to Order, etc.')

    def get_absolute_url(self):
        """Returns URL to access a particular user instance."""
        return reverse('directory:user_detail', args=[str(self.user_id)])

    def __str__(self):
        return self.user_id

    
class Idea(models.Model):
    """Model representing an Idea that a user shares with other others."""
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='ideas')
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
        return self.title

    def get_absolute_url(self):
        return reverse('directory:idea_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

