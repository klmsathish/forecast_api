# Generated by Django 3.1.4 on 2020-12-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201202_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postDate',
            field=models.DateTimeField(),
        ),
    ]
