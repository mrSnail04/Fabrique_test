from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator


class Mailing(models.Model):
    date_time_start = models.DateTimeField(auto_now=False, auto_now_add=False,
                                           verbose_name='Дата и время начала рассылки')
    text_message = models.TextField(verbose_name='Текст сообщения')
    client_filter = models.CharField(max_length=100, verbose_name='Фильтр клиента')
    date_time_finish = models.DateTimeField(auto_now=False, auto_now_add=False,
                                           verbose_name='Дата и время окончания рассылки')

    def __str__(self):
        return "Id рассылки: {}".format(self.id)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

class Client(models.Model):
    phoneNumber = models.CharField(max_length=10, null=False, blank=False,
                                   verbose_name='Телефон в формате 7XXXXXXXXXX (X - цифра от 0 до 9)')
    phoneCode = models.CharField(max_length=3, null=False, blank=False,
                                            verbose_name='Код оператора')
    tag = models.CharField(max_length=100, verbose_name='Тэг')
    timeZone = models.CharField(max_length=3, null=False, blank=False,
                                           verbose_name='Часовая зона UTC')

    def __str__(self):
        return "Id клиента: {}".format(self.id)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Message(models.Model):

    COMPLETED = 'Completed'
    NO_COMPLETED = 'No completed'

    CHOICES = (
        (COMPLETED, 'Выполненно'),
        (NO_COMPLETED, 'Не выполненно'),
    )

    date_time_start = models.DateTimeField(auto_now=False, auto_now_add=False,
                                           verbose_name='Дата и время отправки')
    status = models.CharField(max_length=20, choices=CHOICES, default=NO_COMPLETED,
                                            verbose_name='Статус отправки')
    id_mailing = models.ForeignKey(Mailing, verbose_name='Рассылка', on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, verbose_name='Клиент', on_delete=models.CASCADE)

    def __str__(self):
        return "id сообщение: {}".format(self.id)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
