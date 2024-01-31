from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

VALUE_LETTER = 25


class Group(models.Model):
    """Model group."""

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Слаг поле')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title[VALUE_LETTER]


class Post(models.Model):
    """Model post."""

    text = models.TextField(verbose_name='Текстовое поле')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Поле картинки'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Поле для группы'
    )

    class Meta:
        default_related_name = 'post'

    def __str__(self):
        return self.text[VALUE_LETTER]


class Comment(models.Model):
    """Model comment."""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField(verbose_name='Текстовое поле')
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.text[VALUE_LETTER]
