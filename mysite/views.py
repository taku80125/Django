# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse('Hello World')


from django.shortcuts import render
from .models import Contact



def index(request):
    return render(request,'mysite/index.html')

def about(request):
    return render(request,'mysite/about.html')
def contact(request):
    if request.method =="POST":
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        massage = request.POST.get('massage')
        c=Contact(email=email, subject=subject, massage=massage)
        c.save()
  
        return render(request,'mysite/getback.html')   
    else:
        return render(request,'mysite/contact.html')   

def home(request):
    return render(request,'mysite/home.html')
    
