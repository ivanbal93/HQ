from datetime import datetime

from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(
        default='Название Продукта',
        max_length=100,
        null=False
    )
    author = models.CharField(
        default='Автор',
        max_length=100,
        null=False
    )
    start_datetime = models.DateTimeField(null=False)
    price = models.IntegerField(default=100, null=False)
    group_max = models.IntegerField(default=10, null=False)
    group_min = models.IntegerField(default=1, null=False)

    def __str__(self):
        return (f'{self.name}, '
                f'Время старта {self.start_datetime.strftime("%m/%d/%Y, %H:%M:%S")}, '
                f'Цена {self.price}')

    def lessons_amount(self):
        return Lesson.objects.filter(product__id=self.id).count()


class Lesson(models.Model):
    name = models.CharField(
        default='Название урока',
        max_length=100,
        null=False
    )
    link = models.URLField(null=False)
    product = models.ForeignKey(
        Product,
        related_name='lessons',
        on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.name}, '
                f'Ссылка на урок {self.link}, '
                f'{self.product}')


class Group(models.Model):
    name = models.CharField(
        default='Название группы',
        max_length=100,
        null=False
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.name}, '
                f'{self.product}')


class Student(models.Model):
    name = models.CharField(
        default='Имя студента',
        max_length=100,
        null=False)
    password = models.CharField(
        default='123',
        max_length=8,
        null=False)
    group = models.ManyToManyField(Group, through='StudentGroup')

    def __str__(self):
        return self.name


class StudentGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.group}, '
                f'{self.student}')
