# Generated by Django 5.1.1 on 2024-09-29 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0017_userprofile_phone_number_userprofile_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='deactivated',
            field=models.BooleanField(default=False),
        ),
    ]
