# Generated by Django 2.1.2 on 2019-01-15 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_blogs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='blog_apply_link',
            new_name='blog_view_link',
        ),
    ]
