from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,'invalid credential')
            return redirect('login')

    return render(request,"login.html")



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
             if User.objects.filter(username=username).exists():
                 messages.info(request, 'username taken')
                 return redirect('register')
             # elif User.objects.filter(email=email).exists():
             #     messages.info(request, 'Email taken')
             #     return redirect('register')
             else:
                  user = User.objects.create_user(username=username, password=password)
                  user.save();

                  return redirect('login')

        else:
            messages.info(request, "Password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def newpage(request):
    return render(request,'newpage.html')





def form(request):
    if request.method=="POST":
        prod=User()
        prod.name=request.POST.get('name')
        prod.email=request.POST.get("email")
        prod.dob=request.POST.get("dob")
        prod.address = request.POST.get("address")
        prod.gender = request.POST.get("gender")
        prod.phonenumber = request.POST.get("phonenumber")
        prod.department = request.POST.get("department")
        prod.purpose = request.POST.get("purpose")

        if len(prod.phonenumber ) == 0 :
            messages.info(request, "Please enter valid data")
        else:
            User.save;
            messages.info(request, "Successfully completed")
    return render(request, 'form.html')



        # messages.success
         # return redirect('/')










