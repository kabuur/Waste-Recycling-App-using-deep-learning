# Generated by Django 5.0.6 on 2024-06-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='West_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_Path', models.ImageField(upload_to='Images')),
                ('Prediction', models.CharField(max_length=100)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Type', models.CharField(max_length=50)),
            ],
        ),
    ]
