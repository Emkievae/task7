from django.db import models

# Create your models here.

# создаем класс с описание структуры будущей таблицы
class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)   # подходит для небольших текстов
    description = models.TextField('Описание')    # подходит для больших текстов
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
