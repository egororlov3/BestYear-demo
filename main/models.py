from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now

from users.models import NULLABLE


# ДНЕВНИЕ
class Diary(models.Model):
    situation = models.CharField(max_length=500, verbose_name="Ситуация")
    feelings = models.TextField(verbose_name="Чувства")
    reactions = models.CharField(max_length=250, verbose_name="Рекации", **NULLABLE)
    thoughts = models.TextField(verbose_name="Мысли", **NULLABLE)
    date = models.DateField(verbose_name="Дата", default=now)

    def __str__(self):
        return f"{self.situation} {self.date}"

    class Meta:
        verbose_name = 'дневник'
        verbose_name_plural = 'дневники'


# ПЛАНЫ
class Plans(models.Model):
    plan = models.CharField(max_length=250, verbose_name="План")
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время выполнения", **NULLABLE)
    done = models.BooleanField(default=False, verbose_name="Выполнение")

    def __str__(self):
        return f"{self.plan} {self.date} {self.done} - {'Выполнено' if self.done else 'Не выполнено'}"

    class Meta:
        verbose_name = 'план'
        verbose_name_plural = 'планы'


# ЦЕЛИ НА ГОД
class GoalsYear(models.Model):
    year = models.ForeignKey('YearList', on_delete=models.CASCADE, verbose_name="Год")
    title = models.CharField(max_length=150, verbose_name="Название цели")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    deadline = models.DateField(verbose_name="Срок выполнения", **NULLABLE)

    def __str__(self):
        return f"{self.title} ({self.year.year})"

    # ВАЛИДАЦИЯ ДЕДЛАЙНА
    def clean(self):
        if self.deadline and self.deadline.year != self.year.year:
            raise ValidationError("Дедлайн должен быть в пределах выбранного года.")

    class Meta:
        verbose_name = 'цель на год'
        verbose_name_plural = 'цели на год'


# ЖЕЛАНИЯ
class Wishes(models.Model):
    year = models.ForeignKey('YearList', on_delete=models.CASCADE, verbose_name="Год")
    title = models.CharField(max_length=150, verbose_name="Желание")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"{self.title} ({self.year.year})"

    class Meta:
        verbose_name = 'желание'
        verbose_name_plural = 'желания'


# ПРИВЫЧКИ
class Habits(models.Model):
    year = models.ForeignKey('YearList', on_delete=models.CASCADE, verbose_name="Год")
    title = models.CharField(max_length=200, verbose_name="Привычка")
    is_new = models.BooleanField(default=True, verbose_name="Новая привычка")

    def __str__(self):
        return f"{self.title} ({self.year.year})"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


# БЛАГОДАРНОСТИ
class Thanks(models.Model):
    year = models.ForeignKey('YearList', on_delete=models.CASCADE, verbose_name="Год")
    thank = models.CharField(max_length=250, verbose_name="Благодароность")
    object = models.CharField(max_length=100, verbose_name="Кому/чему", **NULLABLE)

    def __str__(self):
        return f"{self.thank} ({self.year.year})"

    class Meta:
        verbose_name = 'благодарность'
        verbose_name_plural = 'благодарности'


# ЧЕК-ЛИСТ ЗА ГОД
class YearList(models.Model):
    year = models.IntegerField(verbose_name='Год', validators=[MinValueValidator(2000), MaxValueValidator(2100)])

    class Meta:
        verbose_name = 'чек-лист на год'
        verbose_name_plural = 'чек-листы на год'
        ordering = ['year']
