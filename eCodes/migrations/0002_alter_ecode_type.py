# Generated by Django 3.2.7 on 2021-09-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecode',
            name='type',
            field=models.CharField(choices=[('good', 'Халал'), ('doubt', 'Сомнительно'), ('harm', 'Харам')], max_length=100, verbose_name='Тип'),
        ),
    ]
