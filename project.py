from tkinter import *
root = Tk()
root.geometry("390x600")
root.title()
e = Entry(root , width=40, borderwidth=5 )
e.grid(row=0 , column=0,columnspan=3, pady=15)


#function area
def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0, END)

def addition():
    f_number = e.get()
    global f_numb 
    global math 
    math = "addition"
    f_numb = int(f_number)
    e.delete(0 , END)

def substract():
    f_number = e.get()
    global f_numb
    global math
    math = "substract" 
    f_numb = int(f_number)
    e.delete(0 ,END) 

def division():
    f_number = e.get()
    global f_numb 
    global math
    math = "division"
    f_numb = int(f_number)
    e.delete(0 ,END) 


def multiplication():
    f_number = e.get()
    global f_numb 
    global math
    math = "multiplication"
    f_numb = int(f_number)
    e.delete(0 ,END) 


def result():
   second_number = e.get()
   e.delete(0 , END)
   if math == "addition":
       e.insert(0, int(f_numb)+int(second_number))
   elif math == "substract":
       e.insert(0, int(f_numb)-int(second_number))
   elif math == "division":
       e.insert(0, int(f_numb)/int(second_number))
   elif math == "multiplication":
       e.insert(0, int(f_numb)*int(second_number))


#creat calculator buttons
button1 = Button(root , text="1", command=lambda:click(1), padx=30, pady=30)
button2 = Button(root , text="2", command=lambda:click(2), padx=30, pady=30)
button2 = Button(root , text="2", command=lambda:click(2), padx=30, pady=30)
button3 = Button(root , text="3", command=lambda:click(3), padx=30, pady=30)
button4 = Button(root , text="4", command=lambda:click(4), padx=30, pady=30)
button5 = Button(root , text="5", command=lambda:click(5), padx=30, pady=30)
button6 = Button(root , text="6", command=lambda:click(6), padx=30, pady=30)
button7 = Button(root , text="7", command=lambda:click(7), padx=30, pady=30)
button8 = Button(root , text="8", command=lambda:click(8), padx=30, pady=30)
button9 = Button(root , text="9", command=lambda:click(9), padx=30, pady=30)
button0 = Button(root , text="0", command=lambda:click(0), padx=30, pady=30)
button_clear = Button(root , text="clear", command=clear , width=22, pady=30)
addition_button = Button(root , text="+", command=addition , padx=30, pady=30)
substract_button = Button(root , text="-", command=substract , padx=30, pady=30)
division_button = Button(root , text="÷", command=division , padx=30, pady=30)
multiplication_buttuon = Button(root , text="x", command=multiplication , padx=30, pady=30)
result_button = Button(root , text="=", command=result , width=22, pady=30)



# position of the buttons 
button1.grid(row = 3 , column = 0)
button2.grid(row = 3 , column = 1)
button3.grid(row = 3 , column = 2)
button4.grid(row = 2 , column = 0)
button5.grid(row = 2 , column = 1)
button6.grid(row = 2 , column = 2)
button7.grid(row = 1 , column = 0)
button8.grid(row = 1 , column = 1)
button9.grid(row = 1 , column = 2)
button0.grid(row = 4 , column = 0)
button_clear.grid(row = 4 , column=1, columnspan=2)
addition_button.grid(row = 5 , column=0)
substract_button.grid(row = 6 , column=1)
division_button.grid(row = 6 , column=2)
multiplication_buttuon.grid(row= 6 , column=0)
result_button.grid(row = 5 , column = 1, columnspan=2)


root.mainloop()
