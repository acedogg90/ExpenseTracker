# Generated by Django 4.2.7 on 2023-11-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("subtitle", models.CharField(max_length=100)),
                ("authors", models.CharField(max_length=100)),
                ("publisher", models.CharField(max_length=100)),
                ("published_date", models.DateField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("distribution_expense", models.IntegerField()),
            ],
        ),
    ]
