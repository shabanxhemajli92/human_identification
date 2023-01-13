# Generated by Django 4.1.5 on 2023-01-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Human",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("dob", models.DateField()),
                ("address", models.CharField(max_length=100)),
                ("nationality", models.CharField(max_length=100)),
                ("residency", models.CharField(max_length=100)),
                ("bank_account", models.CharField(max_length=100)),
                ("payment_methods", models.CharField(max_length=100)),
                ("cell_phone_provider", models.CharField(max_length=100)),
                ("car_info", models.CharField(max_length=100)),
                ("registration_plate", models.CharField(max_length=100)),
                ("criminal_record", models.CharField(max_length=100)),
                ("photo", models.ImageField(upload_to="photos/")),
            ],
        ),
    ]