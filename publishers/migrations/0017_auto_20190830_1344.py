# Generated by Django 2.1.7 on 2019-08-30 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publishers', '0016_article_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='published',
            new_name='publish',
        ),
    ]
