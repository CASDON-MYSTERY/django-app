# Generated by Django 2.1.7 on 2020-03-04 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0030_auto_20200304_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sections',
            old_name='image_decription',
            new_name='image_description',
        ),
    ]
