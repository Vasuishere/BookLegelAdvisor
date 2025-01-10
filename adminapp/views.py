from django.shortcuts import render,redirect
from userapp.models import contact,appointment,Attorneys,case_categories,Types_Law,Blog
from adminapp.models import adminuser

# Create your views here.
def index(request):
    return render(request,'adminapp/index.html')

def Show_contact(request):
    data = contact.objects.all
    return render(request,'adminapp/contact.html',{"data":data})

def Show_Appointment(request):
    data = appointment.objects.all
    return render(request,'adminapp/appointment.html',{"data":data})

def login(request):
    if request.session.get("islogin"):
        return redirect("/index")
    if request.POST:
        name = request.POST["name"]
        password = request.POST["password"]
        count = adminuser.objects.filter(name=name,password=password).count()
        if count>0:
            request.session['islogin'] = True
            request.session['name'] = name
            return redirect("/index")
    return render(request,'adminapp/login.html')

def logout(request):
    del request.session["islogin"]
    return redirect("/")

def blog(request):
    data = Blog.objects.all
    return render(request,'adminapp/blog.html',{"data":data})


def attorneys(request):
    data = Attorneys.objects.all
    return render(request,'adminapp/attorneys.html',{"data":data})

def case_catogory(request):
    data = case_categories.objects.all
    return render(request,'adminapp/case_categories.html',{"data":data})

def types_Law(request):
    data = Types_Law.objects.all
    return render(request,'adminapp/types_Law.html',{"data":data})




def add_team(request):
    if request.POST:
        name = request.POST["name"]
        profession = request.POST["profession"]
        image = request.POST["image"]
        obj = Attorneys(name=name,profession=profession,image=image)
        obj.save()
        return redirect('/attorneys')
    return render(request,'adminapp/add_team.html')

def demo(request):
    return render(request,'adminapp/demo.html')