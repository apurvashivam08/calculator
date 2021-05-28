from tkinter import *
root=Tk()
root.geometry("228x273")
root.minsize(228,273)
root.maxsize(228,273)
root.title("Calculator")
root.wm_iconbitmap("E:\Python\Projects\Calculator\calc.ico")
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value= int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue=StringVar()
screen=Entry(root,textvariable=scvalue,width=24,font="lucida 12 bold",borderwidth=5)
screen.grid(row=0,column=0,columnspan=4)


button1=Button(root,text="1",padx=20,pady=10)
button1.bind("<Button-1>", click)
button2=Button(root,text="2",padx=20,pady=10)
button2.bind("<Button-1>", click)
button3=Button(root,text="3",padx=20,pady=10)
button3.bind("<Button-1>", click)
button4=Button(root,text="4",padx=20,pady=10)
button4.bind("<Button-1>", click)
button5=Button(root,text="5",padx=20,pady=10)
button5.bind("<Button-1>", click)
button6=Button(root,text="6",padx=20,pady=10)
button6.bind("<Button-1>", click)
button7=Button(root,text="7",padx=20,pady=10)
button7.bind("<Button-1>", click)
button8=Button(root,text="8",padx=20,pady=10)
button8.bind("<Button-1>", click)
button9=Button(root,text="9",padx=20,pady=10)
button9.bind("<Button-1>", click)
button0=Button(root,text="0",padx=20,pady=10)
button0.bind("<Button-1>", click)
button_add=Button(root,text="+",padx=20,pady=10)
button_add.bind("<Button-1>", click)
button_sub=Button(root,text="-",padx=22,pady=10)
button_sub.bind("<Button-1>", click)
button_mul=Button(root,text="*",padx=22,pady=10)
button_mul.bind("<Button-1>", click)
button_div=Button(root,text="/",padx=22,pady=10)
button_div.bind("<Button-1>", click)
button_clr=Button(root,text="C",padx=20,pady=10)
button_clr.bind("<Button-1>", click)
button_per=Button(root,text="%",padx=18,pady=10)
button_per.bind("<Button-1>", click)
button_equal=Button(root,text="=",width=17,padx=20,pady=10)
button_equal.bind("<Button-1>", click)
button_dot=Button(root,text=".",padx=21.5,pady=10)
button_dot.bind("<Button-1>", click)



button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_per.grid(row=4,column=2)
button_div.grid(row=4,column=3)

button_equal.grid(row=5,column=0, columnspan=3)
button_clr.grid(row=5,column=3)

Label(text="Made by Apurva Shivam").grid(row=6,columnspan=4)

root.mainloop()