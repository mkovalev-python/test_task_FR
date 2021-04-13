from django.contrib.auth.models import User
from django.db import models

class Polls(models.Model):
    name_poll = models.CharField('Название опроса', max_length=255, null=False)
    date_start = models.DateTimeField('Дата старта', null=False, editable=False)
    date_finish = models.DateTimeField('Дата окончания', null=False)
    description = models.TextField('Описание', null=False)

    def __str__(self):
        return self.name_poll

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Questions(models.Model):
    poll = models.ForeignKey(Polls, on_delete=models.CASCADE, related_name='Опрос')
    question = models.CharField('Вопрос', max_length=255, null=False)
    type_question = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='Тип вопроса')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Type(models.Model):
    name_type = models.CharField('Тип вопроса', max_length=255, null=False)

    def __str__(self):
        return self.name_type

    class Meta:
        verbose_name = 'Тип вопроса'
        verbose_name_plural = 'Типы вопросов'


class Choices(models.Model):
    questions = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice = models.CharField('Вариант ответа', null=False, max_length=255)


class Answers(models.Model):
    poll = models.ForeignKey(Polls,on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.CharField('Ответ', max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)