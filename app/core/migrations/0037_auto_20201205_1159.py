# Generated by Django 3.1.4 on 2020-12-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20201205_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postImage',
        ),
        migrations.AddField(
            model_name='post',
            name='postImage',
            field=models.ManyToManyField(blank=True, null=True, to='core.Photo'),
        ),
    ]
