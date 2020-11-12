from django.contrib.auth.models import User
from django.db import models
from pytils.translit import slugify
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from seo.models import SeoModel


class PublicationModel(models.Model):
    pub_update = models.DateField(auto_now=True, verbose_name='Дата обновления публикации')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        abstract = True


class ProfileModel(PublicationModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(verbose_name='Аватарка профиля', upload_to='games/profile/img', null=True, blank=True)
    last_login = models.DateField(verbose_name='Последний раз заходил', auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(user=instance)
    else:
        instance.profilemodel.save()


class GamesModel(SeoModel, PublicationModel):
    name = models.CharField(max_length=200, verbose_name='Название игры')
    slug = models.SlugField(max_length=150, blank=True, null=True, allow_unicode=True, unique=True)
    text = models.TextField(verbose_name='Описание игры', blank=True)
    subscribers = models.ManyToManyField(to=ProfileModel, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == '' or self.slug is None:
            self.slug = slugify(self.name)
        else:
            self.slug = slugify(self.slug)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Игры'
        verbose_name_plural = 'Игры'


class PostModel(PublicationModel):
    text = models.TextField(verbose_name='Сообщение', null=True)
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, verbose_name='Автор')
    game = models.ForeignKey(GamesModel, on_delete=models.CASCADE, verbose_name='Игра', related_name='post')

    def __str__(self):
        return "Пост №" + str(self.id)

    class Meta:
        verbose_name = 'Пост игры'
        verbose_name_plural = 'Посты'