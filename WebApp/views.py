from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from WebApp.forms import SignUpForm
from django.http import  HttpResponseRedirect

# Create your views here.

def Home_page(request):
    return render(request, 'myapp/home.html')

@login_required
def Customer_page(request):
    return render(request, 'myapp/customer.html')

def Logout_page(request):
    return render(request, 'myapp/logout.html')

def Registration_page(request):
    form = SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save(commit=True)
        user.set_password(user.password)
        user.password('CharFild')
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'myapp/registration.html',{'form':form})