# Generated by Django 4.1.1 on 2022-10-06 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cat",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="dog",
            options={"ordering": ["id"]},
        ),
        migrations.AddField(
            model_name="cat",
            name="sex",
            field=models.CharField(
                choices=[("Male", "Male"), ("Female", "Female")],
                default="Male",
                max_length=8,
            ),
        ),
    ]
