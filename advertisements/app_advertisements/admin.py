from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet
from django.utils.html import mark_safe

# класс для кастомизации модели в админке
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'title', 'description', 'auction', 'created_at', 'created_date', 'update_date', 'image', 'image_prev' ] # столбцы для отображения в таблице
    list_filter = ['auction', 'created_at', 'price'] # столбцы по которым будет фильтрация
    actions = ['make_action_as_false', 'make_action_as_true'] # методы для выбранных записей
    fieldsets = (
        ('Общие', {
            "fields":(
                'title', 'description', 'user', 'image',
            ),
        }),
        ('Финансы', {
            "fields": (
                'price', 'auction'
            ),
            'classes': ['collapse']
        }),
    )


    @admin.action(description="Убрать возможность торга")
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False) # обновить значение аукцион у выбранных записей на False

    @admin.action(description="Добавить возможность торга")
    def make_action_as_true(self, request, queryset: QuerySet):
        queryset.update(auction = True)









# подключение модели в админку
admin.site.register(Advertisement, AdvertisementAdmin)

# Register your models here.


def dec(func):
    def wrapper():
        print()
        func()
        print()

    return wrapper()