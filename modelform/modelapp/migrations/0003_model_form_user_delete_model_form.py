# Generated by Django 5.0.9 on 2024-10-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modelapp", "0002_rename_model_feedback_form_model_form"),
    ]

    operations = [
        migrations.CreateModel(
            name="model_form_user",
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
                ("name", models.CharField(max_length=30)),
                ("age", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("mobile", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="model_form",
        ),
    ]