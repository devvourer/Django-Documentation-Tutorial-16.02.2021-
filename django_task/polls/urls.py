from django.urls import path
from .views import *

app_name = 'polls'
urlpatterns = [
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/result/', result, name='results'),
    path('<int:question_id>/vote', vote, name='vote'),
    path('', index, name='index')
]