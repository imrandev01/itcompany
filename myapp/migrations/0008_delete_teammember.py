# Generated by Django 5.0.2 on 2024-03-02 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_team'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]