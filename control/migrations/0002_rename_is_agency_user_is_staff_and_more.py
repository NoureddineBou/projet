# Generated by Django 5.0 on 2024-03-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_agency',
            new_name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]