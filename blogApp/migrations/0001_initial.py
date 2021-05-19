# Generated by Django 3.1.5 on 2021-05-14 23:37

import blogApp.utils
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_tagify.fields
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='untitled', max_length=32)),
                ('url', models.CharField(blank=True, max_length=1024)),
                ('image', models.ImageField(upload_to=blogApp.utils.path_for_banner)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContentSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='untitled section', max_length=32)),
                ('content_source', models.CharField(choices=[('All', 'All'), ('Tag', 'Tag'), ('Custom', 'Custom')], default='Tag', max_length=32)),
                ('sort_by', models.CharField(choices=[('Title', 'Title'), ('Oldest', 'Oldest'), ('Newest', 'Newest'), ('View', 'View'), ('Like', 'Like')], default='Title', max_length=32)),
                ('size', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], default=1)),
                ('section_order', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)], default=1)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='untitled', max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('thumbnail', easy_thumbnails.fields.ThumbnailerImageField(upload_to=blogApp.utils.path_for_article_thumbnail)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Code')),
                ('tags', django_tagify.fields.TagsField(default='', help_text='Press enter or comma after each tag you define.', max_length=1000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(related_name='blog_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='HasTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.tag')),
            ],
        ),
        migrations.CreateModel(
            name='HasContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.post')),
                ('content_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogApp.contentsection')),
            ],
        ),
        migrations.AddField(
            model_name='contentsection',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogApp.tag'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogApp.post')),
            ],
        ),
    ]