# Generated by Django 4.2 on 2023-08-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_indivitualuser_name_indivitualuser_tell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indivitualuser',
            name='userName',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
