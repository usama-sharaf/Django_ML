from django.shortcuts import render
from .models import Person 


from openai import OpenAI
client = OpenAI(api_key="sk-5FnpowQGwh7PgFNI9kMhjsdhbkFJE5aEUmyfe70hAdMy7xrM")


def gpt_process(string_value):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a assistant, explain the answer in easy words"},
        {"role": "user", "content": string_value}
    ]
    )

    return str(completion.choices[0].message.content)


def welcome(request):
    
    return render(request,'base.html')


def aboutme(request):
    
    return render(request,'aboutme.html')


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