# Generated by Django 3.1.4 on 2020-12-24 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20201224_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(blank=True, to='notes.Tag'),
        ),
    ]