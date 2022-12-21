# Generated by Django 4.1.4 on 2022-12-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0012_alter_skiduserdetail_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skiduserdetail',
            name='materials',
            field=models.ManyToManyField(blank=True, related_name='users', to='directory.material'),
        ),
        migrations.AlterField(
            model_name='skiduserdetail',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='users', to='directory.skill'),
        ),
        migrations.AlterField(
            model_name='skiduserdetail',
            name='type_of_work',
            field=models.ManyToManyField(blank=True, help_text='eg: Prototype, Production, Made to Order, etc.', related_name='users', to='directory.worktype'),
        ),
    ]
