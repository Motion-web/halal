# Generated by Django 4.0.1 on 2022-01-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='inn',
        ),
        migrations.AddField(
            model_name='application',
            name='address',
            field=models.CharField(default='', max_length=25, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
