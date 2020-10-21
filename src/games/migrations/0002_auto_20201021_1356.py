# Generated by Django 3.1.2 on 2020-10-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gamesmodel',
            options={'verbose_name': 'Игры', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AlterModelOptions(
            name='profilemodel',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(null=True, upload_to='games/profile/img', verbose_name='Аватарка профиля'),
        ),
    ]