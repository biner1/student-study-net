# Generated by Django 3.2.7 on 2022-07-27 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0011_lectures_vote_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectures',
            name='vote_count',
        ),
    ]