# Generated by Django 4.2.1 on 2023-07-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("appBlog", "0009_alter_post_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=255, null=True)),
                ("message", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
