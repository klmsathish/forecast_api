# Generated by Django 3.1.4 on 2020-12-03 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20201203_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreplylike',
            name='commentReplyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.commentreply'),
        ),
    ]