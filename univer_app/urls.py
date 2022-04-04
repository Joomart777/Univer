from django.urls import path

from univer_app.views import *

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('<int:pk>/', DeleteUpdateRetrieveView.as_view()),

]