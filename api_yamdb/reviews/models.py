from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = (
        ('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')
    )
    email = models.EmailField(max_length=60, unique=True)
    bio = models.CharField(max_length=200, blank=True)
    role = models.CharField(
        max_length=30, choices=ROLE_CHOICES, default='user'
    )

    def save(self, *args, **kwargs):
        if self.role == 'admin':
            self.is_superuser = True
        elif self.role == 'moderator':
            self.is_staff = True
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(
        'Название категории', max_length=256, db_index=True)
    slug = models.SlugField('Короткое название', max_length=50, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=256, db_index=True)
    slug = models.SlugField('Короткое название', max_length=50, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError('Проверьте год!')
    return value


class Title(models.Model):
    name = models.CharField('Название', max_length=256, db_index=True)
    year = models.PositiveSmallIntegerField(
        verbose_name='Год', db_index=True,
        validators=[validate_year])
    description = models.TextField(verbose_name='Описание')
    genre = models.ManyToManyField(
        Genre, verbose_name='Жанр', blank=True)
    category = models.ForeignKey(
        Category, verbose_name='Категория',
        on_delete=models.SET_NULL, related_name="titles",
        blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(models.Model):
    text = models.TextField('Текст ревью', max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        'Рейтинг',
        validators=[MinValueValidator(0, 'Не менее 0'),
                    MaxValueValidator(10, 'Не более 10')]
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        related_name='reviews')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review')
        ]
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField('Комментарий', max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
