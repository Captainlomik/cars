# Generated by Django 3.1.5 on 2021-01-14 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad_person', '0006_auto_20210114_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person_auto',
            old_name='comments',
            new_name='description',
        ),
    ]
