#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[53]:


m=pd.read_pickle('house_price_predictor.pkl')

app=tk.Tk()
app.geometry('600x400')
app.title('House price recomendation tool')
bg=tk.PhotoImage(file='bg1.png')
background_label=tk.Label(app,image=bg)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
def houseprice():
    inc=eval(entry_inc.get())
    Age=eval(entry_age.get())
    Room=eval(entry_room.get())
    pop=eval(entry_pop.get())
    query=pd.DataFrame({'Income':[inc],'House_age':[Age],'Rooms':[Room],'Population':[pop]})
    result.set(round(m.predict(query)[0],2))
    
    
    
label=tk.Variable(app)
label.set('=====HOUSE PRICE RECOMENDATION SYSTEM=====')
tk.Label(app,textvariable=label,font=('Courier',15),fg='blue').pack()

income=tk.Variable(app)
income.set('Enter your income: ')
tk.Label(app,textvariable=income,font=0).place(x=100,y=60)

age=tk.Variable(app)
age.set('Enter the age of House: ')
tk.Label(app,textvariable=age,font=0).place(x=100,y=100)

room=tk.Variable(app)
room.set('Enter the number of rooms(More than 2): ')
tk.Label(app,textvariable=room,font=0).place(x=100,y=140)

population=tk.Variable(app)
population.set('Enter the population in the area: ')
tk.Label(app,textvariable=population,font=0).place(x=100,y=180)

entry_inc=tk.Variable(app)
entry_inc.set('0')
tk.Entry(app,textvariable=entry_inc).place(x=400,y=60,height=20)

entry_age=tk.Variable(app)
entry_age.set('0')
tk.Entry(app,textvariable=entry_age).place(x=400,y=100,height=20)

entry_room=tk.Variable(app)
entry_room.set('0')
tk.Entry(app,textvariable=entry_room).place(x=400,y=140,height=20)

entry_pop=tk.Variable(app)
entry_pop.set('0')
tk.Entry(app,textvariable=entry_pop).place(x=400,y=180,height=20)

tk.Button(app,text='Show price of houses available',command=houseprice,bg='cyan',fg='white',font=0).place(x=200,y=220,height=40)

pricepred=tk.Variable(app)
pricepred.set('The predicted price of your house in $: ')
tk.Label(app,textvariable=pricepred,font=0).place(x=100,y=300)

result=tk.Variable(app)
result.set('')
tk.Label(app,textvariable=result,font=0).place(x=400,y=300)

app.mainloop()


# In[ ]:




