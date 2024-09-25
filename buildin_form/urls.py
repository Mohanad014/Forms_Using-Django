from django.urls import path
from . import views
urlpatterns = [
    path('buildin/',views.b_form, name= 'Buildin'),
]