#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox

master = tk.Tk()
tk.Label(master, text="Author Names").grid(row=0)
tk.Label(master, text="Paper Name").grid(row=1)
tk.Label(master, text="Journal Name").grid(row=2)
tk.Label(master, text="Volume").grid(row=3)
tk.Label(master, text="Volume Number").grid(row=4)
tk.Label(master, text="Page Numbers").grid(row=5)
tk.Label(master, text="Month and Year").grid(row=6)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

#x = tk.StringVar()
def build():
    a = e7.get()
    b = a.split(" ")[0]
    c = b[0:3]
    d = "".join(c)
    e = a.split(" ")[1]
    x = e1.get() + ",''"+e2.get()+"'',"+e3.get()+", vol. "+e4.get()+", no. "+e5.get()+", pp "+e6.get()+","+d+" "+e
    messagebox.showinfo("IEEE Reference", x)
    
Build = Button(master, text="Build", command=build).grid(row=8, column=0)
Quit = tk.Button(master, text="Close", command=master.quit, pady=4).grid(row=8, column=1)

master.mainloop()


# In[ ]:





# In[ ]:




