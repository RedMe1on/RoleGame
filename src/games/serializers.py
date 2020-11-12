from rest_framework import serializers

from .models import GamesModel, PostModel


class PostListSerializers(serializers.ModelSerializer):
    """Вывод списка всех постов по всем играм"""

    class Meta:
        model = PostModel
        fields = '__all__'


class PostDetailSerializers(serializers.ModelSerializer):
    """Вывод поста"""

    class Meta:
        model = PostModel
        fields = ('text', 'game', 'profile')


class PostCreateSerializers(serializers.ModelSerializer):
    """Создание поста"""

    class Meta:
        model = PostModel
        fields = '__all__'


class GameDetailSerializers(serializers.ModelSerializer):
    """Информация по игре и сама игра"""
    subscribers = serializers.StringRelatedField(many=True)
    post = PostDetailSerializers(many=True, read_only=True)

    class Meta:
        model = GamesModel
        fields = '__all__'


class GamesListSerializers(serializers.ModelSerializer):
    """Список фильмов"""

    class Meta:
        model = GamesModel
        fields = '__all__'
