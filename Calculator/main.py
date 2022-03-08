from tkinter import *



root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
counter = -1


def button_click(number):
    global counter
    counter += 1
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    
def button_add(m):
    
    global counter
    counter +=1
    e.insert(counter, m)
    
def button_equal():
    
    u = e.get()
    e.delete(0, END)
    final = eval(u)
    e.insert(0, str(final))
    
    
def button_mult(m):
    global counter
    counter +=1
    e.insert(counter, m)
        
def button_subtract(m):
    global counter
    counter +=1
    e.insert(counter, m)
def button_divide(m):
    global counter
    counter +=1
    e.insert(counter, m)
def button_sq(m):
    global counter
    counter +=1
    e.insert(counter, m)
    
def button_sqroot(m):
    global counter
    counter +=1
    e.insert(counter, m)
    
def button_firstp(m):
    global counter
    counter +=1
    e.insert(counter, m)
def button_secondp(m):
    global counter
    counter +=1
    e.insert(counter, m)
    
    

        
    

button1 = Button(root, text=1, padx= 60, pady=40, command=lambda: button_click(1))
button2 = Button(root, text=2, padx= 60, pady=40, command=lambda: button_click(2))
button3 = Button(root, text=3, padx= 60, pady=40, command=lambda: button_click(3))
button4 = Button(root, text=4, padx= 60, pady=40, command=lambda: button_click(4))
button5 = Button(root, text=5, padx= 60, pady=40, command=lambda: button_click(5))
button6 = Button(root, text=6, padx= 60, pady=40, command=lambda: button_click(6))
button7 = Button(root, text=7, padx= 60, pady=40, command=lambda: button_click(7))
button8 = Button(root, text=8, padx= 60, pady=40, command=lambda: button_click(8))
button9 = Button(root, text=9, padx= 60, pady=40, command=lambda: button_click(9))
button0 = Button(root, text=0, padx= 60, pady=40, command=lambda: button_click(0))

buttonadd = Button(root, text='+', padx=40, pady=40, command=lambda : button_add('+'))
buttonequal = Button(root, text='=', padx=60, pady=40, command=lambda: button_equal())
buttonclear = Button(root, text='clear', padx=60, pady=40, command=lambda: button_clear())
buttonmult = Button(root, text='x', padx=40, pady=40, command=lambda : button_mult('*'))
buttonsub = Button(root, text='-', padx=40, pady=40, command=lambda: button_subtract('-'))
buttondiv = Button(root, text='÷', padx=40, pady=40, command=lambda: button_divide('/'))
buttonsq = Button(root, text='²', padx=40, pady=40, command=lambda: button_sq('**2'))
buttonsqr = Button(root, text='√', padx=40, pady=40, command=lambda: button_sqroot('**(1/2)'))
buttonp1 = Button(root, text='(', padx=40, pady=40, command=lambda: button_firstp('('))
buttonp2 = Button(root, text=')', padx=40, pady=40, command=lambda: button_firstp(')'))



button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

buttonadd.grid(row=1, column=3)
buttonequal.grid(row=4, column=2)
buttonclear.grid(row=4, column=1)
buttonmult.grid(row=2, column =3)
buttonsub.grid(row=3, column=3)
buttondiv.grid(row=4, column=3)
buttonsq.grid(row=5, column=1)
buttonsqr.grid(row=5, column=0)
buttonp1.grid(row=5, column=2)
buttonp2.grid(row=5, column=3)



root.mainloop()
