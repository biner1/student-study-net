# Generated by Django 3.1.3 on 2021-10-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='permissions',
            field=models.CharField(choices=[('uploader', 'uploader'), ('student', 'student')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
