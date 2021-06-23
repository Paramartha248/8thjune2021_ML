#GUI of a simple calculator
import tkinter as tk                     
app=tk.Tk()                               
app.title('CALCULATOR')              
app.geometry('300x450')

  
value=tk.Variable(app)
entry=tk.Entry(app,textvariable=value,width=30,font=10)
entry.place(x=10,y=40,height=30)
global expression
expression=""
def operate(e):
    global expression                           
    expression=expression+e
    value.set(expression)
    
def result(n):
    global expression
    r=eval(expression)
    value.set(r)
    expression=""
    
    
def clear():
    global expression
    entry.delete(0,'end')
    expression=""
    
    
tk.Button(app,text='+',height=2,width=4,font=5,command=lambda:operate('+')).place(x=230,y=80)
tk.Button(app,text='-',height=2,width=4,font=5,command=lambda:operate('-')).place(x=230,y=170)
tk.Button(app,text='x',height=2,width=4,font=5,command=lambda:operate('*')).place(x=230,y=260)
tk.Button(app,text='/',height=2,width=4,font=5,command=lambda:operate('/')).place(x=230,y=350)

tk.Button(app,text='1',height=2,width=4,font=5,command=lambda:operate('1')).place(x=20,y=260)
tk.Button(app,text='2',height=2,width=4,font=5,command=lambda:operate('2')).place(x=90,y=260)
tk.Button(app,text='3',height=2,width=4,font=5,command=lambda:operate('3')).place(x=160,y=260)
tk.Button(app,text='4',height=2,width=4,font=5,command=lambda:operate('4')).place(x=20,y=170)
tk.Button(app,text='5',height=2,width=4,font=5,command=lambda:operate('5')).place(x=90,y=170)
tk.Button(app,text='6',height=2,width=4,font=5,command=lambda:operate('6')).place(x=160,y=170)
tk.Button(app,text='7',height=2,width=4,font=5,command=lambda:operate('7')).place(x=20,y=80)
tk.Button(app,text='8',height=2,width=4,font=5,command=lambda:operate('8')).place(x=90,y=80)
tk.Button(app,text='9',height=2,width=4,font=5,command=lambda:operate('9')).place(x=160,y=80)
tk.Button(app,text='0',height=2,width=4,font=5,command=lambda:operate('0')).place(x=90,y=350)
tk.Button(app,text='.',height=2,width=4,font=5,command=lambda:operate('.')).place(x=20,y=350)
tk.Button(app,text='=',height=2,width=4,font=5,command=lambda:result('=')).place(x=160,y=350)
tk.Button(app,text='C',width=4,command=clear).place(x=20,y=10)

app.mainloop()     
                     



            