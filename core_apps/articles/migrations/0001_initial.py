# Generated by Django 3.2.11 on 2022-08-18 01:56

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='article')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('body', models.TextField(verbose_name='article content')),
                ('banner_image', models.ImageField(default='/house_sample.jpg', upload_to='', verbose_name='banner image')),
                ('views', models.IntegerField(default=0, verbose_name='article views')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag', models.CharField(max_length=80)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['tag'],
            },
        ),
        migrations.CreateModel(
            name='ArticleViews',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(max_length=250, verbose_name='ip address')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_views', to='articles.article')),
            ],
            options={
                'verbose_name': 'Total views on Article',
                'verbose_name_plural': 'Total Article Views',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articles', to='articles.Tag'),
        ),
    ]
