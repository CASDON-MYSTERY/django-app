# Generated by Django 2.1.7 on 2019-11-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0024_auto_20191018_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='mod_date',
            field=models.DateTimeField(null=True),
        ),
    ]
