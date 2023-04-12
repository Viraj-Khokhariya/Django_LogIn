from django.shortcuts import render,redirect
from .models import Register

# Create your views here.
def FirstPage(request):
    return render(request,"app/first.html")

def ShowPage(request):
    data1 = Register.objects.all()
    return render(request,"app/table.html",{'key':data1})

def LoginPage(request):
    return render(request,"app/login.html")

def InsertData(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        user = Register.objects.filter(Email=email)
        
        if user:
            message = "User already Exist"
            return render(request,"app/first.html",{'msg':message})
        else:
            if password == cpassword:
                data = Register.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "User Register Successfully"
                return render(request,"app/login.html",{'msg':message})     
            else:
                message = "Password Does not Match"
                return render(request,"app/first.html",{'msg':message})
            
def LoginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = Register.objects.get(Email=email)
            if user.Password == password:
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                request.session['Contact'] = user.Contact
                return render(request,"app/show.html")
            else:
                message = "Password Does not Match"
        except Register.DoesNotExist:
            message = "User Does not Exist"
        
        return render(request,"app/login.html",{'msg':message})
    else:
        return render(request,"app/register.html")

            