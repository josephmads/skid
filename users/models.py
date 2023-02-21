from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from phone_field import PhoneField

User=get_user_model()

# Create your models here.

class Material(models.Model):
    """
    Model representing the materials a user works with. Overwrites save 
    method to make all materials lowercase.
    """
    material = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.material

    def save(self, *args, **kwargs):
        self.material = self.material.lower()
        return super(Material, self).save(*args, **kwargs)

class Skill(models.Model):
    """
    Model representing the skills a user has. Overwrites save 
    method to make all skills lowercase.
    """
    skill = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.skill

    def save(self, *args, **kwargs):
        self.skill = self.skill.lower()
        return super(Skill, self).save(*args, **kwargs)

class WorkType(models.Model):
    """
    Model representing the type of work a user can do. Overwrites save 
    method to make all work types lowercase.
    """
    work_type = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.work_type

    def save(self, *args, **kwargs):
        self.work_type = self.work_type.lower()
        return super(WorkType, self).save(*args, **kwargs)

class Profile(models.Model):    
    """Model extending the User model providing more personal information."""
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100, blank=True)
    email_public = models.EmailField(
        'Public Email',
        blank=True,
        null=True,
        max_length=100, 
        )
    phone_number = PhoneField(blank=True)
    address = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state_province = models.CharField('State or Province', max_length=100, blank=True)
    zip_code = models.CharField('Zip or Postal Code', max_length=10, blank=True)
    country = models.CharField(max_length=56, blank=True)
    about = models.TextField(blank=True)

    skills = models.ManyToManyField(
        to=Skill, 
        related_name='profile', 
        blank=True, 
        help_text='hold ctrl or cmd to select more than one'
        )
    materials = models.ManyToManyField(
        to=Material, 
        related_name='profile', 
        blank=True,
        help_text='hold ctrl or cmd to select more than one'
        )
    type_of_work = models.ManyToManyField(
        to=WorkType,
        related_name='profile', 
        blank=True,
        help_text='hold ctrl or cmd to select more than one'
        )

    def get_absolute_url(self):
        """Returns URL to access a particular user instance."""
        return reverse('directory:user_detail', args=[str(self.user_id)])
    
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
        self.slug = slugify(value, allow_unicode=False)
        super().save(*args, **kwargs)

class Comment(models.Model):
    """Model representing a Comment that a user makes on an Idea."""
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representing the Comment."""
        return f'Comment {self.text} by {self.commenter}'
        
