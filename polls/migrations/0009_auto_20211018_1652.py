# Generated by Django 3.1.3 on 2021-10-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_lecturevote_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturevote',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
