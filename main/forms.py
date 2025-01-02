from time import timezone
from django import forms
from .models import Diary, Plans, GoalsYear, Wishes, Habits, Thanks, YearList


class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["situation", "feelings", "reactions", "thoughts", "date"]


class PlansForm(forms.ModelForm):
    class Meta:
        model = Plans
        fields = ["plan", "date", "done"]


class GoalsYearForm(forms.ModelForm):
    class Meta:
        model = GoalsYear
        fields = ["year", "title", "description", "deadline"]

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        # Пример валидации дедлайна
        if deadline < timezone.now().date():
            raise forms.ValidationError("Дедлайн не может быть в прошлом!")
        return deadline


class WishesForm(forms.ModelForm):
    class Meta:
        model = Wishes
        fields = ["year", "title", "description"]


class HabitsForm(forms.ModelForm):
    class Meta:
        model = Habits
        fields = ["year", "title", "description", "done"]


class ThanksForm(forms.ModelForm):
    class Meta:
        model = Thanks
        fields = ["year", "thank", "object"]


class YearListForm(forms.ModelForm):
    class Meta:
        model = YearList
        fields = ["year"]
