# Generated by Django 4.1.4 on 2023-01-12 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, max_length=100)),
                ('email_public', models.EmailField(help_text='This email address will be displayed on your public SKID profile.', max_length=100, verbose_name='Public Email')),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=150)),
                ('state_province', models.CharField(blank=True, max_length=100, verbose_name='State or Province')),
                ('zip_code', models.CharField(blank=True, max_length=10, verbose_name='Zip or Postal Code')),
                ('country', models.CharField(blank=True, max_length=56)),
                ('about', models.TextField(blank=True)),
                ('materials', models.ManyToManyField(blank=True, related_name='users', to='users.material')),
                ('skills', models.ManyToManyField(blank=True, related_name='users', to='users.skill')),
                ('type_of_work', models.ManyToManyField(blank=True, help_text='eg: Prototype, Production, Made to Order, etc.', related_name='users', to='users.worktype')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(blank=True, default='', max_length=140, null=True, unique=True)),
                ('text', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('d', 'Draft'), ('p', 'Publish')], default='d', max_length=1)),
                ('materials', models.ManyToManyField(blank=True, help_text='Type of materials needed for this Idea.', related_name='idea', to='users.material')),
                ('skills', models.ManyToManyField(blank=True, help_text='Type of skills needed for this Idea.', related_name='idea', to='users.skill')),
                ('type_of_work', models.ManyToManyField(blank=True, help_text='How many do you need made? eg: one = prototype, many = production, etc.', related_name='idea', to='users.worktype')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idea', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
