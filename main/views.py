from collections import defaultdict

from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import DiaryForm, PlansForm, GoalsYearForm, WishesForm, HabitsForm, ThanksForm, YearListForm
from .models import Diary, Plans, GoalsYear, Wishes, Habits, Thanks, YearList


# Main
def main_view(request):
    # Пример данных для отображения на главной странице
    recent_diaries = Diary.objects.order_by('-date')[:5]  # Последние 5 записей из дневника
    upcoming_plans = Plans.objects.filter(done=False).order_by('date')[:5]  # Ближайшие невыполненные планы
    current_year = YearList.objects.order_by('-year').first()  # Текущий год
    goals_for_year = GoalsYear.objects.filter(year=current_year) if current_year else []  # Цели текущего года
    recent_thanks = Thanks.objects.filter(year=current_year)[:3] if current_year else []  # Благодарности текущего года

    context = {
        'recent_diaries': recent_diaries,
        'upcoming_plans': upcoming_plans,
        'current_year': current_year,
        'goals_for_year': goals_for_year,
        'recent_thanks': recent_thanks,
    }

    return render(request, 'main.html', context)


# ДНЕВНИКИ
class DiaryListView(ListView):
    model = Diary
    template_name = "diary_list.html"
    context_object_name = "diaries"


class DiaryDetailView(DetailView):
    model = Diary
    template_name = "diary_detail.html"
    context_object_name = "diary"


class DiaryCreateView(CreateView):
    model = Diary
    template_name = "diary_form.html"
    form_class = DiaryForm
    success_url = reverse_lazy("diary_list")


class DiaryUpdateView(UpdateView):
    model = Diary
    template_name = "diary_form.html"
    form_class = DiaryForm
    success_url = reverse_lazy("diary_list")


class DiaryDeleteView(DeleteView):
    model = Diary
    template_name = "diary_confirm_delete.html"
    success_url = reverse_lazy("diary_list")


# ПЛАНЫ
class PlansListView(ListView):
    model = Plans
    template_name = "plans_list.html"
    context_object_name = "plans"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Сортируем планы по дате (возрастающая дата)
        plans = context['plans'].order_by('date')  # Сортировка по возрастанию даты

        # Группируем планы по дате
        grouped_plans = defaultdict(list)
        for plan in plans:
            grouped_plans[plan.date].append(plan)

        # Ограничиваем количество планов до 3 для каждой даты
        for date in grouped_plans:
            grouped_plans[date] = grouped_plans[date][:3]

        # Передаем сгруппированные планы в контекст
        context['grouped_plans'] = dict(grouped_plans)

        return context

class PlansDetailView(DetailView):
    model = Plans
    template_name = "plans_detail.html"
    context_object_name = "plan"


class PlansCreateView(CreateView):
    model = Plans
    template_name = "plans_form.html"
    form_class = PlansForm
    success_url = reverse_lazy("plans_list")


class PlansUpdateView(UpdateView):
    model = Plans
    template_name = "plans_form.html"
    form_class = PlansForm
    success_url = reverse_lazy("plans_list")


class PlansDeleteView(DeleteView):
    model = Plans
    template_name = "plans_confirm_delete.html"
    success_url = reverse_lazy("plans_list")


# ЦЕЛИ НА ГОД
class GoalsYearListView(ListView):
    model = GoalsYear
    template_name = "goalsyear_list.html"
    context_object_name = "goals"


class GoalsYearDetailView(DetailView):
    model = GoalsYear
    template_name = "goalsyear_detail.html"
    context_object_name = "goal"


class GoalsYearCreateView(CreateView):
    model = GoalsYear
    template_name = "goalsyear_form.html"
    form_class = GoalsYearForm
    success_url = reverse_lazy("goalsyear_list")

    def form_valid(self, form):
        # Дополнительная валидация дедлайна
        try:
            form.instance.clean()
        except ValidationError as e:
            form.add_error("deadline", e)
            return self.form_invalid(form)
        return super().form_valid(form)


class GoalsYearUpdateView(UpdateView):
    model = GoalsYear
    template_name = "goalsyear_form.html"
    form_class = GoalsYearForm
    success_url = reverse_lazy("goalsyear_list")

    def form_valid(self, form):
        try:
            form.instance.clean()
        except ValidationError as e:
            form.add_error("deadline", e)
            return self.form_invalid(form)
        return super().form_valid(form)


class GoalsYearDeleteView(DeleteView):
    model = GoalsYear
    template_name = "goalsyear_confirm_delete.html"
    success_url = reverse_lazy("goalsyear_list")


# ЖЕЛАНИЯ
class WishesListView(ListView):
    model = Wishes
    template_name = "wishes_list.html"
    context_object_name = "wishes"


class WishesDetailView(DetailView):
    model = Wishes
    template_name = "wishes_detail.html"
    context_object_name = "wish"


class WishesCreateView(CreateView):
    model = Wishes
    template_name = "wishes_form.html"
    form_class = WishesForm
    success_url = reverse_lazy("wishes_list")


class WishesUpdateView(UpdateView):
    model = Wishes
    template_name = "wishes_form.html"
    form_class = WishesForm
    success_url = reverse_lazy("wishes_list")


class WishesDeleteView(DeleteView):
    model = Wishes
    template_name = "wishes_confirm_delete.html"
    success_url = reverse_lazy("wishes_list")


# ПРИВЫЧКИ
class HabitsListView(ListView):
    model = Habits
    template_name = "habits_list.html"
    context_object_name = "habits"


class HabitsDetailView(DetailView):
    model = Habits
    template_name = "habits_detail.html"
    context_object_name = "habit"


class HabitsCreateView(CreateView):
    model = Habits
    template_name = "habits_form.html"
    form_class = HabitsForm
    success_url = reverse_lazy("habits_list")


class HabitsUpdateView(UpdateView):
    model = Habits
    template_name = "habits_form.html"
    form_class = HabitsForm
    success_url = reverse_lazy("habits_list")


class HabitsDeleteView(DeleteView):
    model = Habits
    template_name = "habits_confirm_delete.html"
    success_url = reverse_lazy("habits_list")


# БЛАГОДАРНОСТИ
class ThanksListView(ListView):
    model = Thanks
    template_name = "thanks_list.html"
    context_object_name = "thanks"


class ThanksDetailView(DetailView):
    model = Thanks
    template_name = "thanks_detail.html"
    context_object_name = "thank"


class ThanksCreateView(CreateView):
    model = Thanks
    template_name = "thanks_form.html"
    form_class = ThanksForm
    success_url = reverse_lazy("thanks_list")


class ThanksUpdateView(UpdateView):
    model = Thanks
    template_name = "thanks_form.html"
    form_class = ThanksForm
    success_url = reverse_lazy("thanks_list")


class ThanksDeleteView(DeleteView):
    model = Thanks
    template_name = "thanks_confirm_delete.html"
    success_url = reverse_lazy("thanks_list")


# ЧЕК-ЛИСТЫ
class YearListListView(ListView):
    model = YearList
    template_name = "yearlist_list.html"
    context_object_name = "years"


class YearListCreateView(CreateView):
    model = YearList
    template_name = "yearlist_form.html"
    form_class = YearListForm
    success_url = reverse_lazy("yearlist_list")


class YearListUpdateView(UpdateView):
    model = YearList
    template_name = "yearlist_form.html"
    form_class = YearListForm
    success_url = reverse_lazy("yearlist_list")


class YearListDeleteView(DeleteView):
    model = YearList
    template_name = "yearlist_confirm_delete.html"
    success_url = reverse_lazy("yearlist_list")
