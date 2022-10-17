# Generated by Django 4.1.2 on 2022-10-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="")),
                ("price", models.IntegerField()),
                ("specification", models.CharField(max_length=50)),
            ],
        ),
    ]
