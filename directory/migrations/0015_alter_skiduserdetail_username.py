# Generated by Django 4.1.4 on 2022-12-22 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0014_alter_skiduserdetail_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skiduserdetail',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
