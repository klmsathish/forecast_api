# Generated by Django 3.1.3 on 2020-11-23 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201116_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='uname',
            new_name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='to be filled', max_length=255),
            preserve_default=False,
        ),
    ]
