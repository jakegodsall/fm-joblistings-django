# Generated by Django 5.0.2 on 2024-03-06 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'companies'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]