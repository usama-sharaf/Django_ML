from django.shortcuts import render


#from .models import Person



def welcome(request):
    
    return render(request,'base.html')


def aboutme(request):
    
    return render(request,'aboutme.html')


def userINPUT(request):
    result = None
    print("hi")

    
    if request.method == 'POST':

        
        mynum=int(request.POST['number'])
        result = mynum
        print("hello")


    return render(request,'User_input.html' , {'result' : result })