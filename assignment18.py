
"""
#Q.1
1.From which keyword we import the Tkinter in program?
a.	 call
b.	 from
c.	 import
d.	All of the above
Ans:c
2.	How pack() function works on tkinter widget ?
a.	According to x,y coordinate
b.	According to row and column vise
c.	According to left,right,up,down
d.	None of the above
Ans:c
3.	How the grid() function put the widget on the screen ?
a.	According to x,y coordinate
b.	According to row and column vise
c.	According to left,right,up,down
d.	None of the above
Ans:b
4.	Tkinter tool in python provide the
a.	Database
b.	OS commands
c.	GUI
d.	All of the above
Ans:c
5.Which of the following is not a geometry managers are available in Tkinter?
a.	 .pack( )
b.	 .grid( )
c.	 .place( )
d.	 .flex()
Ans:d
6.Which one is not a valid Tkinter widgets? 
a.  Label
b.  Button
c.  Entry
d.  WebBrowser
Ans:d
Q.2 Write a GUI program to show the images selected by the user .

#Using the tkinter PhotoImage
from tkinter import *
from tkinter import filedialog as fd

def load():
   f= fd.askopenfilename()
   v1.set(f)
   return

def show():
    img= PhotoImage(file=v1.get())
    L=Label(w,  image=img)
    L.grid(row=3,column=0)
    L.image=img
    return


w = Tk()
w.geometry("700x500")

v1=StringVar()
Label(w, text='FileName').grid(row=1,column=0)
Entry(w,text=v1).grid(row=1,column=1)
Button(w, text='Load', command=load).grid(row=2,column=2)
Button(w, text='Show', command=show).grid(row=2,column=3)

w.mainloop()

#Q.3 Write a GUI program to show the graph based on user selection on the data available in CSV file.

#Using the tkinter PhotoImage
from tkinter import *
from tkinter import filedialog as fd
import pandas as pd
import matplotlib.pyplot as plt


def load():
   f= fd.askopenfilename()
   f1.set(f)
   return

def plotgraph():
    df=pd.read_csv( f1.get())
    fig=plt.figure()
    if v1.get()==1 : plt.bar( df[ df.columns[0]] , df [ df.columns[1]] )
    if v1.get()==2 : plt.plot(df[ df.columns[0]] , df [ df.columns[1]])
    if v1.get()==3 : plt.scatter(df[ df.columns[0]] , df [ df.columns[1]])
    plt.xticks(rotation=15)
    plt.savefig('f:/g1.png')

def show():
    plotgraph()
    img= PhotoImage(file='f:/g1.png')
    L=Label(w,  image=img)
    L.grid(row=5,column=4)
    L.image=img
    return


w = Tk()
w.geometry("700x500")

v1=IntVar()
f1=StringVar()
v1.set(1)

Label(w, text='FileName').grid(row=1,column=0)
Entry(w,text=f1).grid(row=1,column=1)
Button(w, text='Load CSV', command=load).grid(row=2,column=2)

Radiobutton(w, text='Bar', variable=v1, value=1).grid(row=3, column=1)
Radiobutton(w, text='Line', variable=v1, value=2).grid(row=3, column=2)
Radiobutton(w, text='Scatter', variable=v1, value=3).grid(row=3, column=3)

Button(w, text='Show Graph', command=show).grid(row=4,column=3)


w.mainloop()
"""












