from django.db import models

from django.contrib import admin
from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.




class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/')

    # если запись создана сегодня то отображение зеленым если нет то серым
    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():  # проверяем что запись была создана сегодня
            created_time = self.created_at.time().strftime('%H.%M.%S')
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",
                created_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H.%M.%S')

    @admin.display(description='дата обновления')
    def update_date(self):
        if self.updated_at.date() == timezone.now().date():  # проверяем что запись была создана сегодня
            created_time = self.updated_at.time().strftime('%H.%M.%S')
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня в {}</span>",
                created_time
            )
        return self.updated_at.strftime('%d.%m.%Y at %H.%M.%S')

    @admin.display(description='изображение')
    def image_prev(self):
        if self.image:
            return format_html(
                '<img src="{}" style="width: 55px;">', self.image.url
            )
        else:
            return 'No Image'



    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price}) "
    class Meta:
        db_table = "advertisements"

class Advertisements(models.Model):
    text = models.CharField(max_length=64)

    def __str__(self):
        return self.text






