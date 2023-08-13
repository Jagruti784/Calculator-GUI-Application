from tkinter import *

first_number=second_number=operator=None

def get_digit(digit):    #Defining a function get_digit and having a 'digit' parameter inside it which will be printed later while calling the function
    current = result_label['text']      #Putting result_label object inside var 'current'. Putting list inside as it is changeable and allows multiple duplicate values for a calculator ex. 77
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')
    
def get_operator(op):
    global first_number, operator  #. The global keyword is used to indicate that the function should use the global scope variables with these names, rather than creating local variables with the same names within the function.
    
    first_number = int (result_label['text'])  #Storing the result_label (result screen text) in first_number variable After clicking on operator that is saving the first number
    operator=op
    result_label.config(text='')  #Emptying the label of result after clicking operator
    
def get_result():
    global first_number, second_number, operator
    
    second_number = int(result_label['text'])
    
    if operator == '+':
        result_label.config(text=str(first_number+second_number))
    elif operator == '-':
        result_label.config(text=str(first_number-second_number))
    elif operator == '*':
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error') # Cannot be divided by zero
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))   #Rounding the result up to two decimal places by using (round,...2)
        

root = Tk()  #object of Tk class
root.title('Calculator')        #name of the object root
root.geometry('280x380')           #size
root.resizable(0,0)            #no movements in x, y axis i.e fixed
root.configure(background='black')

result_label=Label(root, text='', bg='black', fg='white')  #Creating a Object variable 'result_label' of 'Label' class inside which is placed 'root' Object with text '0', background colour=black and font colour=white
result_label.grid(row=0, column=0, columnspan= 5, pady=(50,25), sticky='w')  #Calling grid and placing the resul_label in the first row of grid layout and first column is for the text  0's position. Column span is mentioned so that the UI doesn't tear. pady is for y axis-vertical padding around a widget.  This specifies vertical padding around the widget. The (50, 25) values are a tuple, where the first value (50) indicates the padding above the widget, and the second value (25) indicates the padding below the widget. sticky 'w' indicates the text will start from west side insted of center
result_label.config(font=('verdana', 30, 'bold' ))      #Configuring result_label's font to Verdana, size 30 and making it bold

btn7 = Button(root, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(7)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white. Command Lambda function is Linking get_digit function with the user interface '7' text
btn7.grid(row=1, column=0)
btn7.config(font=('verdana', 14))

btn8 = Button(root, text='8', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(8)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn8.grid(row=1, column=1)
btn8.config(font=('verdana', 14))

btn9 = Button(root, text='9', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(9)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn9.grid(row=1, column=2)
btn9.config(font=('verdana', 14))

btn_add = Button(root, text='+', bg='#00a65a', fg='white', width=5, height=2, command=lambda : get_operator('+')) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn_add.grid(row=1, column=3)
btn_add.config(font=('verdana', 14))


btn4 = Button(root, text='4', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(4)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn4.grid(row=2, column=0)
btn4.config(font=('verdana', 14))

btn5 = Button(root, text='5', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(5)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn5.grid(row=2, column=1)
btn5.config(font=('verdana', 14))

btn6 = Button(root, text='6', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(6)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn6.grid(row=2, column=2)
btn6.config(font=('verdana', 14))

btn_sub = Button(root, text='-', bg='#00a65a', fg='white', width=5, height=2, command=lambda : get_operator('-')) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('verdana', 14))

btn1 = Button(root, text='1', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(1)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn1.grid(row=3, column=0)
btn1.config(font=('verdana', 14))

btn2= Button(root, text='2', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(2)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn2.grid(row=3, column=1)
btn2.config(font=('verdana', 14))

btn3 = Button(root, text='3', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(3)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn3.grid(row=3, column=2)
btn3.config(font=('verdana', 14))

btn_mul = Button(root, text='*', bg='#00a65a', fg='white', width=5, height=2, command=lambda : get_operator('*')) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn_mul.grid(row=3, column=3)
btn_mul.config(font=('verdana', 14))

btn_clr = Button(root, text='C', bg='#00a65a', fg='white', width=5, height=2, command=lambda :clear()) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn_clr.grid(row=4, column=0)
btn_clr.config(font=('verdana', 14))

btn0 = Button(root, text='0', bg='#00a65a', fg='white', width=5, height=2, command=lambda :get_digit(0)) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn0.grid(row=4, column=1)
btn0.config(font=('verdana', 14))

btn_equals = Button(root, text='=', bg='#00a65a', fg='white', width=5, height=2, command=get_result) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn_equals.grid(row=4, column=2)
btn_equals.config(font=('verdana', 14))

btn_div = Button(root, text='/', bg='#00a65a', fg='white', width=5, height=2, command=lambda : get_operator('/')) #Creating new object of variable 'btn7' with class 'Button' inside which root is placed with text string '7' background colour with a shade of teel and font colour white
btn_div.grid(row=4, column=3)
btn_div.config(font=('verdana', 14))

root.mainloop()
