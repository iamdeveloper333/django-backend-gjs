# Generated by Django 2.1.1 on 2018-10-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20181003_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
