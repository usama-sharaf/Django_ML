from django.shortcuts import render, redirect
from .models import Person 
from django.contrib.auth.decorators import login_required







from openai import OpenAI
client = OpenAI(api_key="sk-5FnpowQGwh7PgFNI9kMhjsdhbkFJE5aEUmyfe70hAdMy7xrM")


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login ,logout


def gpt_process(string_value):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a assistant, explain the answer in easy words"},
        {"role": "user", "content": string_value}
    ]
    )

    return str(completion.choices[0].message.content)

@login_required
def welcome(request):
    
    return render(request,'base.html')

@login_required
def aboutme(request):
    
    return render(request,'aboutme.html')

@login_required
def userINPUT(request):
    result = None
    print("hi")

    
    if request.method == 'POST':

        
        user_input_text=str(request.POST['text'])
        try:
            gpt_output=gpt_process(user_input_text)
            result = gpt_output
            
            myinstance = Person(userinputvalue = user_input_text , mycalvalue = gpt_output)
            myinstance.save()
        except:
            pass




    return render(request,'User_input.html' , {'result' : result })


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Change 'home' to the name of your home page URL
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('welcome')  # Change 'home' to the name of your home page URL
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_fun(request):
    logout(request)
    return redirect('login')


@login_required
def csv_img_fun(request):
    if request.method == 'POST':
        # Assuming you have a form with a csrf_token and file fields named 'csvFile' and 'imageFile'
        csv_file = request.FILES.get('csvFile')
        image_file = request.FILES.get('imageFile')
        print(csv_file)
        print(image_file)

    return render(request,'csv_image.html')