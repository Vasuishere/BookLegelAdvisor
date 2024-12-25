from django.shortcuts import render, redirect
from pyexpat.errors import messages

from userapp.models import user,contact,Attorneys,Client_Review,Blog,Types_Law,Practice_Area,case_categories,case_studies


# Create your views here.
def login(request):
    if request.session.get("islogin"):
        return redirect("/")
    elif request.POST:
        e = request.POST["email"]
        p = request.POST["password"]
        count = user.objects.filter(email=e, password=p).count()
        if count > 0:
            request.session['islogin'] = True
            request.session['email'] = e
            return redirect("/")
    return render(request, "login.html")


def signup(request):
    if request.POST:
        n = request.POST['name']
        e = request.POST['email']
        nu = request.POST['number']
        p = request.POST['password']
        obj = user(name=n, email=e, number=nu, password=p)
        obj.save()
        return redirect("/home")
    return render(request, "signup.html")


def index(request):
    data = Attorneys.objects.all
    review_data = Client_Review.objects.all
    Blog_data = Blog.objects.all
    Types = Types_Law.objects.all
    return render(request, "index.html",{"data":data,"review_data":review_data,"Blog":Blog_data,"Types_Law":Types})


def about(request):
    data = Attorneys.objects.all
    return render(request, "about.html",{"data":data})


def blog(request):
    Blog_data = Blog.objects.all
    return render(request, "blog.html",{"Blog":Blog_data})


def contact1(request):
    if request.POST:
        n = request.POST['name']
        e = request.POST['email']
        s = request.POST['subject']
        m = request.POST['message']
        obj = contact(name=n,email=e,subject=s,message=m)
        obj.save()
        return redirect("/contact1")
    return render(request, "contact.html")


def portfolio(request):
    data = case_categories.objects.all
    data1 = case_studies.objects.all
    return render(request, "portfolio.html",{"data":data,"data1":data1})


def service(request):
    Types = Types_Law.objects.all
    return render(request, "service.html",{"Types_Law":Types})


def single(request):
    return render(request, "single.html")


def team(request):
    data = Attorneys.objects.all
    return render(request, "team.html",{"data":data})


def appointment(request):
    return render(request, "appointment.html")


def header(request):
    return render(request, "header.html")


def logout(request):
    del request.session['islogin']
    return redirect("/")

def law_readmore(request,id):
    data = Practice_Area.objects.filter(pid = id).all()
    return render(request,"law_readmore.html",{"data":data})
