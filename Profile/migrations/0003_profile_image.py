# Generated by Django 5.1.1 on 2024-10-03 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_rename_owner_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_kstxax', upload_to='images/'),
        ),
    ]
