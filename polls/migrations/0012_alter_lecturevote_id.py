# Generated by Django 3.2.7 on 2021-10-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20211031_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturevote',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
