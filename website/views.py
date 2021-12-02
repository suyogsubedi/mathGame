from django.shortcuts import render

def home(request):
    return render(request, 'home.html',{})

def addition(request):
    from random import randint 
    
    number1 = randint(0,20)
    number2 = randint(0,20)
   
    if request.method == "POST":
       
        answer = request.POST['answer']
        old_number1=request.POST['old_number1']
        old_number2=request.POST['old_number2']
        correct_answer =int(old_number1) +int(old_number2)
        if int(answer) == correct_answer:
            my_answer = "Bravo, Right Answer " + old_number1 + "+" + old_number2 + "=" + answer
            color ="primary"
            
        else:
            my_answer="Incorrect " + old_number1 + "+" + old_number2 + "=" + str(correct_answer)
            color ="danger"

        return render(request,'addition.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
            })
 
    return render(request, 'addition.html',{
        'number1':number1,
        'number2':number2,
    })

def subtraction(request):
    from random import randint 
    
    number1 = randint(0,20)
    number2 = randint(0,20)
   
    if request.method == "POST":
       
        answer = request.POST['answer']
        old_number1=request.POST['old_number1']
        old_number2=request.POST['old_number2']
        correct_answer =int(old_number1) -int(old_number2)
        if int(answer) == correct_answer:
            my_answer = "Bravo, Right Answer " + old_number1 + "-" + old_number2 + "=" + answer
            color ="primary"
            
        else:
            my_answer="Incorrect " + old_number1 + "-" + old_number2 + "=" + str(correct_answer)
            color ="danger"

        return render(request,'subtraction.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
            })
 
    return render(request, 'subtraction.html',{
        'number1':number1,
        'number2':number2,
    })

def multiplication(request):
    from random import randint 
    
    number1 = randint(0,20)
    number2 = randint(0,20)
   
    if request.method == "POST":
       
        answer = request.POST['answer']
        old_number1=request.POST['old_number1']
        old_number2=request.POST['old_number2']
        correct_answer =int(old_number1) * int(old_number2)
        if int(answer) == correct_answer:
            my_answer = "Bravo, Right Answer " + old_number1 + "*" + old_number2 + "=" + answer
            color ="primary"
            
        else:
            my_answer="Incorrect " + old_number1 + "*" + old_number2 + "=" + str(correct_answer)
            color ="danger"

        return render(request,'multiplication.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
            })
 
    return render(request, 'multiplication.html',{
        'number1':number1,
        'number2':number2,
    })



def division(request):
    return render(request, 'division.html',{})

# Game
def game(request):
    return render(request,'game.html')

# Learn

def learn(request):
    return render(request,'learn.html')