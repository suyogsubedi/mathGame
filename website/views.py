from django.shortcuts import render

"""
This view redners the homepage of the application
"""
def home(request):
    return render(request, 'home.html',{})

"""
This view renders the addition page 

Generates two random numbers

Checks the answer provided by the user and provides a feedback
"""
def addition(request):
    from random import randint 
    
    number1 = randint(0,20)
    number2 = randint(0,20)
   
    if request.method == "POST":
       
        answer = request.POST['answer']
        old_number1=request.POST['old_number1']
        old_number2=request.POST['old_number2']
        """
         Checking for empty or alphabetical values
        """
        if not answer.isdigit() or not answer:
            my_answer= "Empty or alphabetical submission are not accepted"
            color= 'warning'
            return render(request,'addition.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
          
            })
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

"""
This view renders the subtraction page 

Generates two random numbers

Checks the answer provided by the user and provides a feedback
"""
def subtraction(request):
    from random import randint 
    
    number1 = randint(0,20)
    number2 = randint(0,20)
   
    if request.method == "POST":
       
        answer = request.POST['answer']
        old_number1=request.POST['old_number1']
        old_number2=request.POST['old_number2']
        """
         Checking for empty or alphabetical values
        """
        if not answer.isdigit() or not answer:
            my_answer= "Empty or alphabetical submission are not accepted"
            color= 'warning'
            return render(request,'subtraction.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
          
            })
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

"""
This view renders the subtraction page 

Generates two random numbers

Checks the answer provided by the user and provides a feedback
"""
def multiplication(request):
    from random import randint 
    
    number1 = randint(0,20)
    number2 = randint(0,20)
   
    if request.method == "POST":
       
        answer = request.POST['answer']
        old_number1=request.POST['old_number1']
        old_number2=request.POST['old_number2']
        """
         Checking for empty or alphabetical values
        """
        if not answer.isdigit() or not answer:
            my_answer= "Empty or alphabetical submission are not accepted"
            color= 'warning'
            return render(request,'multiplication.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
          
            })        
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

"""
This view renders the division page 

Generates two random numbers

Checks the answer provided by the user and provides a feedback
"""

def division(request):
    from random import randint 
    
    number1 = randint(0,20)
    number2 = randint(1,5)
   
    if request.method == "POST":
       
        answer = request.POST['answer']
        old_number1=request.POST['old_number1']
        old_number2=request.POST['old_number2']
        """
         Checking for empty or alphabetical values
        """

        if not answer.isdigit() or not answer:
            my_answer= "Empty or alphabetical submission are not accepted"
            color= 'warning'
            return render(request,'division.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
          
            })

        correct_answer =int(old_number1) / int(old_number2)
        if float(answer) == correct_answer:
            my_answer = "Bravo, Right Answer " + old_number1 + "/" + old_number2 + "=" + answer
            color ="primary"
            
        else:
            my_answer="Incorrect " + old_number1 + "/" + old_number2 + "=" + str(correct_answer)
            color ="danger"

        return render(request,'division.html',{
            'answer':answer,
            'my_answer':my_answer,
            'number1':number1,
            'number2':number2,
            'color':color,
            })
 
    return render(request, 'division.html',{
        'number1':number1,
        'number2':number2,
    })


# Game

"""
This view renders the Game page

The main logic behind this game is provided by JavaScript
"""
def game(request):
    return render(request,'game.html')

# Learn
"""
This view renders the Learn Page

The main logic behind this learning page is provided by JavaScript
"""
def learn(request):
    return render(request,'learn.html')