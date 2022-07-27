from django.urls import path
from .views import SignupView, AccountDestroyView, ListView

urlpatterns = [
    path('', ListView.as_view()),
    path('signup/', SignupView.as_view()),
    path('delete/<email>/', AccountDestroyView.as_view()),

]