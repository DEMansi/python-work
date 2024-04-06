from django.shortcuts import render
from.models import Contact,User
# Create your views here.
def index(request):
     return render(request,'index.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
                name=request.POST['name'],
	            email=request.POST['email'],
	            mobile=request.POST['mobile'],
	            remarks=request.POST['remarks']
			)
		msg="Contact Saved Successfully"
		contact=Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'msg':msg,'contact':contact})
	else:
		contact=Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'contact':contact})    

def signup(request):
	if request.method=="POST":
		User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
	            email=request.POST['email'],
	            mobile=request.POST['mobile'],
                address=request.POST['address'],
	            password=request.POST['password']
	        )
		msg="User Sign Up Successfully"
		return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')   

def login(request):
     return render(request,'login.html')         