from django.shortcuts import render, redirect
from .form import UserProfileForm
from .models import User

def user_input(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Model_Output')
    else:
        form = UserProfileForm()
    return render(request, 'm_input.html', {'form': form})

def user_output(request):
    profiles = User.objects.all()
    return render(request, 'm_output.html', {'profiles': profiles})
