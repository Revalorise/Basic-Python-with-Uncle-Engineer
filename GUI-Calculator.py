from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() 
GUI.title('โปรเเกรมคำณวณราคาน้ำมัน ไฮพรีเมียม ดีเซล S B7')
GUI.geometry('700x600')

bg = PhotoImage(file='ถังน้ำมัน.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนลิตร',font=(None,20))
L.pack()

v_quantity = StringVar() 
E1 = ttk.Entry(GUI, textvariable = v_quantity, font=(None,20))
E1.pack()

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 46 
        messagebox.showinfo('Total Price', 'Total Cost of Gas is {} Baht'.format(calc) )
        v_quantity.set('1')
        E1.focus()
    except:
        messagebox.showwarning('Wrong type of input', 'Please insert numbers only')
        v_quantity.set('1')
        E1.focus()

B = ttk.Button(GUI, text='Calculate',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) #ipadx ขยายควางกว้าง x/y

GUI.mainloop() #เพื่อให้โปรเเกรมรันตลอดเวลา