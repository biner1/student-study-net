# Generated by Django 3.2.7 on 2021-09-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_lecturevote_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturevote',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]