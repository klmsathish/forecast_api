# Generated by Django 3.1.4 on 2020-12-03 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20201203_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='commentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comment'),
        ),
        migrations.RemoveField(
            model_name='commentlike',
            name='userId',
        ),
        migrations.AddField(
            model_name='commentlike',
            name='userId',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='commentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comment'),
        ),
        migrations.RemoveField(
            model_name='commentreply',
            name='userId',
        ),
        migrations.AddField(
            model_name='commentreply',
            name='userId',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='commentreplylike',
            name='commentReplyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comment'),
        ),
        migrations.RemoveField(
            model_name='commentreplylike',
            name='userId',
        ),
        migrations.AddField(
            model_name='commentreplylike',
            name='userId',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postDescription',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='storyview',
            name='storyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.story'),
        ),
        migrations.RemoveField(
            model_name='storyview',
            name='userId',
        ),
        migrations.AddField(
            model_name='storyview',
            name='userId',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
