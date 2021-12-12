from django.shortcuts import render


def home(request):
    """
    This view redners the homepage of the application
    """
    return render(request, 'home.html',{})


def addition(request):
    """
    This view renders the addition page 

    Generates two random numbers

    This function only accepts integer input

    Checks the answer provided by the user and provides a feedback
    """
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



def subtraction(request):
    """
    This view renders the subtraction page 

    Generates two random numbers

    This function only accepts integer input

    Checks the answer provided by the user and provides a feedback
    """
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


def multiplication(request):
    """
    This view renders the multiplication page 

    Generates two random numbers from 0 to 20

    This function only accepts integer input

    Checks the answer provided by the user and provides a feedback
    """
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



def division(request):
    """
    This view renders the addition page 

    Generates two random numbers, one from 0 to 20 and the other from 1 to 5

    This function only accepts integer input

    Checks the answer provided by the user and provides a feedback
    """
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


def game(request):
    """
    This view renders the Game page

    The main logic behind this game is provided by JavaScript which is linked with game.html page
    """
    return render(request,'game.html')

# Learn

def learn(request):
    """
    This view renders the Learn Page

    The main logic behind this learning page is provided by JavaScript which is linked with learn.html page
    """
    return render(request,'learn.html')