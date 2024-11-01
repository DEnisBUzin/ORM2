from django.db import models


class TagsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_main=True)


class Tag(models.Model):

    name = models.CharField(max_length=50,
                            verbose_name='Название тэга',)

    class Meta:
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='Scope')

    class Meta:

        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    objects = models.Manager()
    tags_manager = TagsManager()

    def __str__(self):
        return self.title


class Scope(models.Model):

    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='scopes')
    tag = models.ForeignKey(Tag,
                            on_delete=models.CASCADE,
                            verbose_name='Имя тега',
                            related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Главный')

    class Meta:
        verbose_name_plural = 'Теги в статьях'
        # ordering = 'is_main'
        ordering = ['-is_main', 'tag__name']
    objects = models.Manager()
    tags_manager = TagsManager()




