from django.shortcuts import render

# Create your views here.

def input(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        return render(request,'output.html',{'name':name,'email':email,'password':password,'contact':contact, 'address':address})
    return render(request,'input.html')
