from django.urls import path
from . import views
urlpatterns = [
    path('mform/',views.user_input, name= 'Model_Input'),
    path('moutput/',views.user_output, name= 'Model_Output'),
]