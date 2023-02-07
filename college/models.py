from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Problem(models.Model):
    # uther = models.ForeignKey(Author, on_delete=models.CASCADE)
    pro_id = models.CharField(max_length=1000)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=11)
    description=models.CharField(max_length=500)
    city=models.CharField(max_length=20)
    e_email=models.EmailField(max_length=30)
    picture=models.ImageField(upload_to="images")
    college=models.CharField(max_length=40)
    date=models.DateField()
    mode = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')

class Comment(models.Model):
	post = models.ForeignKey(Problem, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()

class SubComment(models.Model):
	post = models.ForeignKey(Problem, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    college_address = models.CharField(max_length=100)
    hostel = models.CharField(max_length=50)
    room_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

class Deta(models.Model):
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=100)
    hostel = models.CharField(max_length=50)
    room_no = models.CharField(max_length=5)
    year = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
class Hostel(models.Model):
    name_warden = models.CharField(max_length=30)
    hostel_name = models.CharField(max_length=30)
    wanden_email = models.EmailField(max_length=30)
    tstudent = models.CharField(max_length=100)
    total_empty_rooms = models.CharField(max_length=50)
    total_alloted_room = models.CharField(max_length=50)
    tfloor = models.CharField(max_length=10)
class Mess_timetable(models.Model):
    hostel_name = models.CharField(max_length=30)
    secretary_name = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=40)
    sunday_breakfast = models.CharField(max_length=30)
    sunday_lunch = models.CharField(max_length=30)
    sunday_snack = models.CharField(max_length=30)
    sunday_dinner = models.CharField(max_length=30)
    monday_breakfast = models.CharField(max_length=30)
    monday_lunch = models.CharField(max_length=30)
    monday_snack = models.CharField(max_length=30)
    monday_dinner = models.CharField(max_length=30)
    tuesday_breakfast = models.CharField(max_length=100)
    tuesday_lunch = models.CharField(max_length=100)
    tuesday_snack = models.CharField(max_length=100)
    tuesday_dinner = models.CharField(max_length=100)
    wednesday_breakfast = models.CharField(max_length=50)
    wednesday_lunch  = models.CharField(max_length=50)
    wednesday_snack = models.CharField(max_length=50)
    wednesday_dinner = models.CharField(max_length=50)
    thursday_breakfast = models.CharField(max_length=50)
    thursday_lunch = models.CharField(max_length=50)
    thursday_snack = models.CharField(max_length=50)
    thursday_dinner = models.CharField(max_length=50)
    friday_breakfast = models.CharField(max_length=40)
    friday_lunch = models.CharField(max_length=40)
    friday_snack = models.CharField(max_length=40)
    friday_dinner = models.CharField(max_length=40)
    sarturday_breakfast = models.CharField(max_length=40)
    sarturday_lunch = models.CharField(max_length=40)
    sarturday_snack = models.CharField(max_length=40)
    sarturday_dinner = models.CharField(max_length=40)

class Entry(models.Model):
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=30)
    room_no = models.CharField(max_length=5)
    work = models.CharField(max_length=5)
    hostel = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)