# Generated by Django 2.1.7 on 2019-11-26 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0025_auto_20191125_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_heading',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
