from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .apps import MainConfig
from .views import main_view

app_name = MainConfig.name

urlpatterns = [
    path('', main_view, name='main'),

    # Маршруты для дневника
    path('diaries/', views.DiaryListView.as_view(), name='diary_list'),
    path('diaries/<int:pk>/', views.DiaryDetailView.as_view(), name='diary_detail'),
    path('diaries/create/', views.DiaryCreateView.as_view(), name='diary_create'),
    path('diaries/<int:pk>/update/', views.DiaryUpdateView.as_view(), name='diary_update'),
    path('diaries/<int:pk>/delete/', views.DiaryDeleteView.as_view(), name='diary_delete'),

    # Маршруты для планов
    path('plans/', views.PlansListView.as_view(), name='plans_list'),
    path('plans/<int:pk>/', views.PlansDetailView.as_view(), name='plans_detail'),
    path('plans/create/', views.PlansCreateView.as_view(), name='plans_create'),
    path('plans/<int:pk>/update/', views.PlansUpdateView.as_view(), name='plans_update'),
    path('plans/<int:pk>/delete/', views.PlansDeleteView.as_view(), name='plans_delete'),

    # Маршруты для целей на год
    path('goals/', views.GoalsYearListView.as_view(), name='goals_list'),
    path('goals/<int:pk>/', views.GoalsYearDetailView.as_view(), name='goals_detail'),
    path('goals/create/', views.GoalsYearCreateView.as_view(), name='goals_create'),
    path('goals/<int:pk>/update/', views.GoalsYearUpdateView.as_view(), name='goals_update'),
    path('goals/<int:pk>/delete/', views.GoalsYearDeleteView.as_view(), name='goals_delete'),

    # Маршруты для желаний
    path('wishes/', views.WishesListView.as_view(), name='wishes_list'),
    path('wishes/<int:pk>/', views.WishesDetailView.as_view(), name='wishes_detail'),
    path('wishes/create/', views.WishesCreateView.as_view(), name='wishes_create'),
    path('wishes/<int:pk>/update/', views.WishesUpdateView.as_view(), name='wishes_update'),
    path('wishes/<int:pk>/delete/', views.WishesDeleteView.as_view(), name='wishes_delete'),

    # Маршруты для привычек
    path('habits/', views.HabitsListView.as_view(), name='habits_list'),
    path('habits/<int:pk>/', views.HabitsDetailView.as_view(), name='habits_detail'),
    path('habits/create/', views.HabitsCreateView.as_view(), name='habits_create'),
    path('habits/<int:pk>/update/', views.HabitsUpdateView.as_view(), name='habits_update'),
    path('habits/<int:pk>/delete/', views.HabitsDeleteView.as_view(), name='habits_delete'),

    # Маршруты для благодарностей
    path('thanks/', views.ThanksListView.as_view(), name='thanks_list'),
    path('thanks/<int:pk>/', views.ThanksDetailView.as_view(), name='thanks_detail'),
    path('thanks/create/', views.ThanksCreateView.as_view(), name='thanks_create'),
    path('thanks/<int:pk>/update/', views.ThanksUpdateView.as_view(), name='thanks_update'),
    path('thanks/<int:pk>/delete/', views.ThanksDeleteView.as_view(), name='thanks_delete'),

    # Маршруты для чек-листов на год
    path('yearlists/', views.YearListListView.as_view(), name='yearlist_list'),
    path('yearlists/create/', views.YearListCreateView.as_view(), name='yearlist_create'),
    path('yearlists/<int:pk>/update/', views.YearListUpdateView.as_view(), name='yearlist_update'),
    path('yearlists/<int:pk>/delete/', views.YearListDeleteView.as_view(), name='yearlist_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
