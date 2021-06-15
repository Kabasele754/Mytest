From tkinter import *

def btnCliick(number):
    global operator
	operator = operator + str(number)
	text_input.set(operator)

def btnClearDiplay():
	global operator
	operator = ""
	text_input.set("")
	
def btnEgalsDisplay():
	global operator
	sumup = str(eval(operator))
	text_input.set(sumup)
	operator =""
	
cal = TK()
cal.title("Calculator")
operator =""
text_input = StringVar()

txDisplay = Entry(cal, font=('arial', 20 , 'bold'),textvariable=text_input,bd=30, insertwidtn =4'
				 bg="powder blue", justify='right').grid(columnspan=4)

btn7 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20 , 'bold'),
			  text="7",command=lambda:btnCliick(7),bg="powder red").grid(row1, columns=0)


btn8 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20 , 'bold'),
			  text="8",command=lambda:btnCliick(8),bg="powder red").grid(row1, columns=1)

btn9 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20 , 'bold'),
			  text="9",command=lambda:btnCliick(9),bg="powder red").grid(row1, columns=2)
			  
Additiom = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20 , 'bold'),
			  text="+",command=lambda:btnCliick(+),bg="powder red").grid(row1, columns=3)
			  
cal.mainloop()
	
	