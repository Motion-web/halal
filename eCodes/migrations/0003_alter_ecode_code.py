# Generated by Django 3.2.8 on 2021-10-23 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCodes', '0002_alter_ecode_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecode',
            name='code',
            field=models.CharField(max_length=15, verbose_name='Код'),
        ),
    ]
