from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from test1.models import *


def index(request):
    feedata=Feedback.objects.all()
    if request.method == 'POST':
        type = request.POST.get("type")
        if type == "login":
            name = request.POST.get("Username")
            Password = request.POST.get("password")
            check = User.objects.filter(name=name, password=Password)
            if check:
                request.session["Username"] = name
                return render(request, 'Home.html',{'feedata':list(feedata) })
            else:
                return render(request, "login.html", {"error": "Invalid Username or password"})
        elif type == "signup":
            name = request.POST.get("Username")
            Password = request.POST.get("password")
            cpass = request.POST.get("cpassword")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            check = User.objects.filter(name=name)
            if len(mobile)>10:
                return render (request,'signup.html', {"error": "Invalid Mobile no."})
            elif len(mobile)<10:
                return render (request,'signup.html', {"error": "Invalid Mobile no."})
            if check:
                return render(request, 'signup.html', {"error": "user already exist"})
            else:
                if Password != cpass:
                    return render(request, 'signup.html', {"error": "password doesn't match"})
                else:
                    obj = User.objects.create(
                        name=name, password=Password, email=email, mobile=mobile)
                    obj.save()
                    return render(request, "login.html", {"error": "Account created successfully! Please Login"})
    return render(request, 'Home.html',{'feedata':list(feedata) })


def logout(request):
    del request.session['Username']
    return redirect('/')


def navbar(request):
    return render(request, 'nav.html')


def footer(request):
    return render(request, 'footer.html')


def Menu(request):
    return render(request, 'Menu.html')


def about(request):
    return render(request, 'about.html')


def cookies(request):
    return render(request, 'cookies.html')


def beverages(request):
    return render(request, 'beverages.html')


def sweets(request):
    return render(request, 'sweets.html')


def desserts(request):
    return render(request, 'desserts.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')

def checkout(request):
    chk = request.GET.get('item')
    if chk == "none":
        return render(request, 'cart.html', {'error': "No items to checkout"})
    elif chk == "yes":
        return render(request, 'checkout.html')
    else:
        return HttpResponse(status=403)


def mycart(request):
    prices = [99, 119, 149, 159, 199, 119, 209, 219, 219, 249, 269, 129, 299, 299, 399, 499, 40, 45, 50, 55, 50, 60, 70, 80]
    if request.method == "POST":
        user = request.session.get("Username")
        name = request.POST.get("Product-name")
        pid = int(request.POST.get("Product-id"))
        action = request.POST.get('action')
        if user is None:
            return redirect('/login')
        try:
            exist = cart.objects.get(product_id=pid, user=user)
            if action == "add":
                exist.quantity += 1
                exist.save()
                return render(request, "menu.html")
            else:
                exist.quantity -= 1
                if exist.quantity < 1:
                    exist.delete()
                else:
                    exist.save()
                return redirect('/cart')
        except:
            if action == "remove":
                return render(request, 'cart.html', {'error': "Item does not exist in cart"})
            else:
                p = prices[pid-1]
                object = cart.objects.create(product_id=pid, product_name=name, quantity=1, price=p, user=user)
                object.save()
                return render(request, "menu.html")
    else:
        user = request.session.get("Username")
        if user is None:
            return redirect('/login')
        else:
            all=cart.objects.filter(user=user)
            all=list(all)
            total = 0
            if len(all)<1:
                all=None
            else:
                for i in all:
                    total = total + (i.price * i.quantity)
            return render(request, 'cart.html', {"data":all, "total": total})
        
def fb(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        feedback=request.POST['feedback']
        obj=Feedback(name=name,email=email,feedback=feedback)
        obj.save()
        return redirect('/')
    
    return render(request,"feedback.html")

def popup(request):
    return render(request, 'popup.html')

def fav(request):
    return request(request, "fav.html")
