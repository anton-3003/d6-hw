from django.db import models


# модель издательства: название
class Publisher(models.Model):
    pub_name = models.TextField()

    def __str__(self):
        return self.pub_name


# модель автора: Ф.И., год рождения, страна
class Author(models.Model):
    full_name = models.TextField(verbose_name="Имя")
    birth_year = models.SmallIntegerField(verbose_name="Год рождения")
    country = models.CharField(verbose_name="Страна", max_length=2)

    def __str__(self):
        # return self.full_name
        return "{}, {}".format(self.full_name, self.birth_year)


# модель книги: международный код, название, описание, год "создания", автор, количество экз., цена, издательство

class Book(models.Model):
    ISBN = models.CharField(verbose_name="Международный код", max_length=13)
    title = models.TextField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year_release = models.SmallIntegerField(verbose_name="Год издания")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author", verbose_name="Автор")
    copy_count = models.SmallIntegerField(verbose_name="Количество экз.")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, related_name="books",
                                  verbose_name="Издательство")

    def __str__(self):
        return self.title
