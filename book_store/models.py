from django.db import models
from django.contrib.auth.models import User
class Categories(models.Model):
    name = models.CharField(verbose_name="Назва жанру", max_length=40)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Author(models.Model):
    first_name = models.CharField(verbose_name="Ім'я", max_length=100)
    last_name = models.CharField(verbose_name="Прізвище", max_length=100)
    date_of_birth = models.DateField(verbose_name="Дата народження", null=True, blank=True)
    date_of_death = models.DateField(verbose_name="Дата смерті", null=True, blank=True)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(self.first_name) + " " + str(self.last_name)


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    score = models.PositiveSmallIntegerField(
        choices=(
            (1, "★☆☆☆☆"),
            (2, "★★☆☆☆"),
            (3, "★★★☆☆"),
            (4, "★★★★☆"),
            (5, "★★★★★"),
        )
    )
    title = models.CharField(max_length=180)
    content = models.CharField(max_length=900)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return ", ".join((str(self.author), str(self.book)))

    class Meta:
        ordering = ["-timestamp"]
        unique_together = ("author", "book",)


class book(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=50)
    description = models.CharField(verbose_name="Опис", max_length=1500)
    price = models.FloatField(verbose_name="Ціна")
    count = models.IntegerField(verbose_name="Кількість")
    photo = models.ImageField(verbose_name="Фото")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    categories = models.ManyToManyField(Categories, help_text="Select a genre for this book", verbose_name='Категорії')
    pages = models.IntegerField(verbose_name="Сторінок")
    shoppers = models.ManyToManyField(
        User,
        related_name="shopping_cart",
        blank=True,
        editable=False
    )

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class status_order(models.Model):
    name = models.CharField(verbose_name="Назва", max_length=50)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Клієнт')
    adress = models.CharField(verbose_name="Адреса", max_length=200)
    phone = models.CharField(verbose_name="Телефон", max_length=200)
    book = models.ForeignKey('book', on_delete=models.SET_NULL, null=True, verbose_name='Книга')
    date_start = models.DateField(null=True, blank=True, verbose_name='Дата відправки')
    date_finish = models.DateField(null=True, blank=True, verbose_name='Дата прибуття')
    count = models.IntegerField(verbose_name="Кількість")
    price = models.FloatField(verbose_name="Ціна")
    status = models.ForeignKey('status_order',blank=True, on_delete=models.SET_NULL, null=True, verbose_name='Статус замовлення')


    class Meta:
        managed = True
class ActivationLink(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=36)

    def __str__(self):
        return str(self.user) + ":" + self.link

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    book = models.ForeignKey(
        "Book",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    score = models.PositiveSmallIntegerField(
        choices=(
            (1, "★☆☆☆☆"),
            (2, "★★☆☆☆"),
            (3, "★★★☆☆"),
            (4, "★★★★☆"),
            (5, "★★★★★"),
        )
    )
    title = models.CharField(max_length=180)
    content = models.CharField(max_length=900)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return ", ".join((str(self.author), str(self.book)))

    class Meta:
        ordering = ["-timestamp"]
        unique_together = ("author", "book",)







