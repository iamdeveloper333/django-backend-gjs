# Generated by Django 2.1.1 on 2018-10-02 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20181002_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
