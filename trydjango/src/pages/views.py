from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(request.user) # for getting user, prints in terminal
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html",{})

def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    my_context = {
        'my_contact1': '123456789',
        'my_contact2': '987654321'
    }
    return render(request,"contact.html",my_context)