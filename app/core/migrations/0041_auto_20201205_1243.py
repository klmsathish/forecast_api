# Generated by Django 3.1.4 on 2020-12-05 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20201205_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='postImage',
        ),
        migrations.AddField(
            model_name='post',
            name='postImage',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.photo'),
        ),
    ]
