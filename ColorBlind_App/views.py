from django.shortcuts import render
from ColorBlind_App.models import Color
from ColorBlind_App.forms import NewUserForm

def index(request):
    return render(request,"html/index.html")

def results(rocky):
    webpage_list = Color.objects.order_by('-id')[:1][::-1]
    date_dict = {'access_record':webpage_list}
    return render(rocky,'html/results.html',context=date_dict)

def colors(request):
    form=NewUserForm()

    if request.method=="POST":
        form=NewUserForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return results(request)
    else:
        print("Error occured")

    return render(request,"html/test.html",{"form":form})


def contact(request):
    return render(request,"html/contact-us.html")

def login(request):
    return render(request,"html/login.html")

def reg(request):
    return render(request,"html/registration.html")
