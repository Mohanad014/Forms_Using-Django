from django.shortcuts import render
#from . import form

# to call the function without class name
from .form import MyForm

def b_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            return render(request, 'b_output.html', {'name': name, 'age': age, 'email': email, 'address': address})
    else:
        form = MyForm()
    return render(request, 'b_input.html',{'form': form})


