# Generated by Django 4.2.7 on 2023-11-18 20:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_book_table"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="book",
            table="book_expenses",
        ),
    ]
