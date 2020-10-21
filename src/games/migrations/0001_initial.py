# Generated by Django 3.1.2 on 2020-10-20 16:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_update', models.DateField(auto_now=True, verbose_name='Дата обновления публикации')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GamesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.MaxLengthValidator(100)], verbose_name='Тайтл для поисковых систем')),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)], verbose_name='Описание для поисковых систем')),
                ('pub_update', models.DateField(auto_now=True, verbose_name='Дата обновления публикации')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('name', models.CharField(max_length=200, verbose_name='Название игры')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=150, null=True, unique=True)),
                ('text', models.TextField(blank=True, verbose_name='Описание игры')),
                ('subscribers', models.ManyToManyField(to='games.ProfileModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]