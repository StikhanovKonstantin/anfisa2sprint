from django.db import models

from core.models import PublishedModel


# В этой таблице хранятся категории мороженого:
class Category(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True,
                            verbose_name='Слаг')
    output_order = (
        models.PositiveSmallIntegerField(default=100,
                                         verbose_name='Порядок отображения')
                                         )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


# В этой таблице хранятся все топпинги для мороженного:
class Topping(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self) -> str:
        return self.title


# В этой таблице хранятся обёртки, упаковки для мороженого.
class Wrapper(PublishedModel):
    title = models.CharField(
        max_length=256,
        verbose_name='Название',
        help_text='Уникальное название обёртки, не более 256 символов.'
        )

    class Meta:
        verbose_name = 'Обёртка'
        verbose_name_plural = 'Обёртки'

    def __str__(self) -> str:
        return self.title


# В этой таблице хранятся мороженое.
class IceCream(PublishedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обёртка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топинги')
    is_on_main = models.BooleanField(default=False, verbose_name='На главной')
    output_order = (
        models.PositiveSmallIntegerField(default=100,
                                         verbose_name='Порядок отображения')
                                         )
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Мороженное'
        verbose_name_plural = 'Мороженки'
        ordering = ('output_order', 'title')

    def __str__(self) -> str:
        return self.title
