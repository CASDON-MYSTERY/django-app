# Generated by Django 2.1.7 on 2020-03-05 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0031_auto_20200304_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_description',
            field=models.CharField(blank=True, default='image', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sections',
            name='image_description',
            field=models.CharField(blank=True, default='image', max_length=255, null=True),
        ),
    ]
