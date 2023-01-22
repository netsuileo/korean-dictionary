# Generated by Django 4.1.3 on 2023-01-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("words", "0003_rename_meading_word_meaning"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="word",
            name="word_class",
        ),
        migrations.AlterField(
            model_name="word",
            name="origin",
            field=models.CharField(
                blank=True, max_length=64, null=True, verbose_name="Origin"
            ),
        ),
    ]