from django.shortcuts import render, redirect,HttpResponse
from .models import Problem, Contact,Deta,Hostel,Mess_timetable,Entry
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from .forms import ImageForm

# Create your views here.
def home(request):
    if request.user.is_superuser:
        mydata1 = Problem.objects.all()
    else:
        username = request.user.username
        mydata1 = Problem.objects.filter(name=username)
    if request.method=="POST":
        # data fetch
        name = request.user.username
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        description = request.POST.get('description')
        email= request.POST.get('email')
        college = request.POST['colleges']
        date = request.POST.get('date')
        images = request.FILES['upload']
        # print(name, l_name,phone,city, description,email,college,date)
        
        f= Problem()
        f.name=name
        f.phone=phone
        f.city = city
        f.description=description
        f.e_email = email
        f.college = college
        f.date = date
        f.picture = images
        f.mode = 'Pending'
        f.save()
        messages.success(request, 'Problem is informed successfully')
        return redirect('/')
    return render(request, 'home.html',{'data1':mydata1})

def showdata(request, pro_id):
    mydata1=Problem.objects.get(pk=pro_id)
    if request.method=="POST":
        status = request.POST.get('option_in')
        p = Problem.objects.get(pk=pro_id)
        p.mode = status
        p.save()
        messages.success(request, 'Status update successfully')
        print('************************save')
        return redirect('/')

    return render(request, 'show_problem.html',{'data':mydata1})
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        print(first_name,last_name,username, password,confirm_password)
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'user is already exist')
                print('*************exist already')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password, email=email, first_name=first_name,last_name=last_name)
                user.set_password(password)
                user.save()
                # print('Successfull save')
                messages.success(request, 'Create a user successfully')
                return redirect('loginup')
    else:
        return render(request, 'signup.html')
def loginup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username and password")
            return redirect('loginup')
    else:
        return render(request, 'loginup.html')

def logoutup(request):
    auth.logout(request)
    return redirect('signup')

def contact(request):
    if request.method == 'POST':
        address_us = request.POST.get('address')
        hostel_us = request.POST.get('hostel')
        phone_us = request.POST.get("phone")
        room_us = request.POST.get("room")
        name = request.user
        print(address_us,hostel_us,phone_us,name)
        if name and room_us and phone_us and address_us and hostel_us is not None:
            c = Contact()
            c.name = name
            c.college_address = address_us
            c.hostel = hostel_us
            c.phone = phone_us
            c.room_number = room_us
            c.save()
            messages.success(request, 'Contact request is send successfully')
            return redirect('/')
        else:
            return redirect('/')
    # else:
    #     return redirect('contact')
    data = Contact.objects.all()
    
    return render(request, 'contact.html',{'data':data})
def details(request):
    data = Deta.objects.all()
    return render(request, 'deta.html',{'data':data})
def student(request):
    
    if request.method=="POST":
    # data fetch
        name = request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        hostel = request.POST.get('hostel')
        email= request.POST.get('email')
        branch = request.POST.get('branch')
        room = request.POST.get('room')
        year = request.POST.get('year')
        print(name,phone,address,hostel,email,branch,room,year)
        d = Deta()
        d.name = name
        d.phone = phone
        d.address = address
        d.hostel = hostel
        d.email = email
        d.branch = branch
        d.room_no = room
        d.year = year
        d.save()

        messages.success(request, 'Save successfully')
        return redirect('student')
    else:
        return render(request, 'studentdata.html')

    return render(request, 'studentdata.html')

def detail_update(request,pro_id):
    
    U = Deta.objects.get(pk=pro_id)
    if request.method=="POST":
    # data fetch
        name = request.POST.get('name')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        hostel = request.POST.get('hostel')
        email= request.POST.get('email')
        branch = request.POST.get('branch')
        room = request.POST.get('room')
        year = request.POST.get('year')
        print(name,phone,address,hostel,email,branch,room,year)
        d = Deta(pk=pro_id)
        d.name = name
        d.phone = phone
        d.address = address
        d.hostel = hostel
        d.email = email
        d.branch = branch
        d.room_no = room
        d.year = year
        d.save()
        messages.success(request, 'Update successfully')
        return redirect('details')
    return render(request, 'student_update.html',{"item":U})

def hostel(request):
    detail_hostel = Hostel.objects.all()
    return render(request, 'hostel.html',{"data":detail_hostel})
def messup(request):
    timetable = Mess_timetable.objects.all()
    return render(request, 'mess.html',{'timetable':timetable})
def need(request):
    timetable = Mess_timetable.objects.all()
    return render(request, 'requ.html')
def index(request):
    timetable = Mess_timetable.objects.all()
    return render(request, 'index.html')
def entry(request):
    if request.method=="POST":
    # data fetch
        name = request.POST.get('name')
        roll=request.POST.get('roll')
        room =request.POST.get('room')
        work = request.POST.get('work')
        # time = request.POST.get('branch')
        hostel = request.POST.get('hostel')
        # print(name,phone,address,hostel,email,branch,room,year)
        E = Entry()
        E.name = name
        E.roll = roll
        E.room_no = room
        E.work = work
        E.hostel = hostel
        E.save()
        messages.success(request, 'Update successfully')
        return redirect('/')

    E = Entry.objects.all()
    return render(request, 'entry.html',{'data':E})
