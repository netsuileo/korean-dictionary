# Generated by Django 4.1.3 on 2023-01-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("words", "0006_remove_word_origin_remove_word_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="word",
            name="meaning",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="Meaning"
            ),
        ),
    ]