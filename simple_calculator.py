from tkinter import*
root=Tk()
root.title("simple calculator")

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)


def button_click(number):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(number))
def button_add():
    first_number=e.get()
    global fn
    global math
    fn=int(first_number)
    math="addition"
    e.delete(0,END)
def button_sub():
    first_number=e.get()
    global fn
    global math
    fn=int(first_number)
    math="subtraction"
    e.delete(0,END)
def button_mul():
    first_number=e.get()
    global fn
    global math
    fn=int(first_number)
    math="multiplication"
    e.delete(0,END)     
def button_div():
    first_number=e.get()
    global fn
    global math
    fn=int(first_number)
    math="division"
    e.delete(0,END)     
def button_equal():
    second_num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,fn+int(second_num))
    if math=="subtraction":
        e.insert(0,fn-int(second_num))
    if math=="multiplication":
        e.insert(0,fn*int(second_num)) 
    if math=="division":
        e.insert(0,fn/int(second_num))
def button_clear():
    e.delete(0,END) 

                       



    

button11 = Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
button22 = Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
button33 = Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
button44=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))    
button55=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
button66=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
button77=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
button88=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
button99=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
button_add1=Button(root,text="x",padx=25,pady=20,command=lambda:button_add())
button_sub1=Button(root,text="-",padx=25,pady=20,command=lambda:button_sub())
button_mul1=Button(root,text="x",padx=25,pady=20,command=lambda:button_mul())
button_div1=Button(root,text="%",padx=25,pady=20,command=lambda:button_div())
button_clear1=Button(root,text="C",padx=40,pady=20,command=lambda:button_clear)
button00=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
button_equal1=Button(root,text="=",padx=40,pady=20,command=lambda:button_equal())

    


button11.grid(row=3,column=0)
button22.grid(row=3,column=1)
button33.grid(row=3,column=2)
button44.grid(row=2,column=0)
button55.grid(row=2,column=1)
button66.grid(row=2,column=2)
button77.grid(row=1,column=0)
button88.grid(row=1,column=1)
button99.grid(row=1,column=2)
button00.grid(row=4,column=1)
button_add1.grid(row=1,column=4)
button_sub1.grid(row=2,column=4)
button_mul1.grid(row=3,column=4)
button_div1.grid(row=4,column=4)
button_clear1.grid(row=4,column=0)
button_equal1.grid(row=4,column=2)

root.mainloop()