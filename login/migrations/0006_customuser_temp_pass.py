# Generated by Django 5.0.3 on 2024-07-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_customuser_pfp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='temp_pass',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
