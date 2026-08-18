"""
#Q.1
1.	Essential thing to create a window screen using tkinter python?
a.	call tk() function
b.	create a button
c.	To define a geometry
d.	To define the frame
Ans:a
2.	fg in tkinter widget is stands for ?
a.	foreground
b.	background
c.	forgap
d.	front group
Ans:a
3.      For user Entry data, which widget we use in tkinter ?
a.	Entry.
b.	Text.
c.	Label.
d.	Message.
Ans:a
4.	How the place() function put the widget on the screen ?
a.	According to x,y coordinate
b.	According to row and column wise
c.	According to left, right,up,down
d.	According to random position.
Ans:a
5.	To change the property of the widget after the declaration of widget, what is used?
a.	mainloop() function
b.	config() function
c.	pack() function
d.	title() function
Ans:b
"""
#Add any 2 numbers
import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result, n1, n2):  
    num1 = (n1.get())  
    num2 = (n2.get())  
    result = int(num1)+int(num2)  
    label_result.config(text="Result = %d" % result)  
    return  
   
root = tk.Tk()  
root.geometry('400x200+100+200')  
  
root.title('Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)  
  
labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)
labelResult = tk.Label(root)  
  
labelResult.grid(row=7, column=2)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)  
  
call_result = partial(call_result, labelResult, number1, number2)  
  
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)  
  
root.mainloop()
#3.To print a table of given number
from tkinter import *

def show_table():
	num = int(entry.get())
	str1=' Table of ' + str(num) + '\n-----------------\n'
	for i in range(1,11):
		str1 = str1 + " " + str(num) + " x " + str(i) + " = " + str(num*i) + "\n"

	output_label.configure(text = str1, justify=LEFT)
	
main_window = Tk()
main_window.title("Perfect Python tkinter Tutorials : www.EasyCodeBook.com")
message_label = Label(text= ' Enter a number to \ndisplay its Table ' ,
font=( ' Verdana ' , 12))
output_label = Label(font=( ' Verdana ' , 12))
entry = Entry(font=( ' Verdana ' , 12), width=6)
calc_button = Button(text= ' Show Multiplication Table ' , font=( ' Verdana ', 12), 
command=show_table)
message_label.grid(row=0, column=0,padx=10, pady=10)
entry.grid(row=0, column=1,padx=10, pady=10, ipady=10)
calc_button.grid(row=0, column=2,padx=10, pady=10)
output_label.grid(row=1, column=0, columnspan=3,padx=10, pady=10)
mainloop()
#4factorial of number
from tkinter import *
f=1
def show_table():
           
	num=int(entry.get())
        
	#str1=' Table of ' + str(num) + '\n-----------------\n'
           
	for i in range(1,num,1):
		num=num*i

	output_label.configure(text =num, justify=LEFT)
	
main_window = Tk()
main_window.title("Perfect Python tkinter Tutorials : www.EasyCodeBook.com")
message_label = Label(text= ' Enter a number to \ndisplay its Table ' ,
font=( ' Verdana ' , 12))
output_label = Label(font=( ' Verdana ' , 12))
entry = Entry(font=( ' Verdana ' , 12), width=6)
calc_button = Button(text= ' Show Multiplication Table ' , font=( ' Verdana ', 12), 
command=show_table)
message_label.grid(row=0, column=0,padx=10, pady=10)
entry.grid(row=0, column=1,padx=10, pady=10, ipady=10)
calc_button.grid(row=0, column=2,padx=10, pady=10)
output_label.grid(row=1, column=0, columnspan=3,padx=10, pady=10)
mainloop()
#5Write a Python GUI program to create a window and set the default window size
#using tkinter module.
import tkinter as tk
parent = tk.Tk()
parent.title("-Welcome to Python tkinter Basic exercises-")
parent.geometry('600x300')
parent.mainloop()








