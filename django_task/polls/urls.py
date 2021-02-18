from django.urls import path
from .views import *

app_name = 'polls'
urlpatterns = [
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/result/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', VoteView.as_view(), name='vote'),
    path('', IndexView.as_view(), name='index')
]