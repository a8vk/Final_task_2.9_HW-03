from django.db import models
from django.contrib.auth.models import User


# Класс Автор
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)  # поле рейтинг автора

    def update_rating(self):  # метод обновление рейтинга
        pass


# Класс Категория
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)  # максимальную длину рекомендуется указывать 2 в n степени


# Класс Сообщение
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # поле автор
    NEWS = 'NW'
    ARTICLE = 'AR'
    # поле выбора
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)  # Автоматически добавлять дату и время создания
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        pass

    def dislike(self):
        pass


# Класс Категория сообщения
class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


# Класс Комментарий
class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)  # даём возможность комментировать пользователю
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        pass

    def dislike(self):
        pass
