from Tkinter import *
from functools import partial


def validateLogin(username, password):
	print ("User has entered the username :", username.get())
	print ("User has entered the password :", password.get())
	return


# Creating the GUI window 
console = Tk () # Initialization of Tkinter
console.geometry('400x300')  # Size of the window
console.title('Login page for using python Tkinter code')


# Creating input of username 
Label1 = Label (console, text="User Name"). grid (row=0, column=0) # Label to specify Username
Input1 = StringVar() 
# Inputing the user’s name
usernameEntry = Entry (console, text variable = Input1). grid (row=0, column=1)  


# Creating input of Password
# Label to specify Login
Label2 = Label(console,text="Password").grid(row=1, column=0)  
Input2 = StringVar()
# Inputing the Password
passwordEntry = Entry (console, text variable = Input2, show='*'). grid (row=1, column=1)  


validateLogin = partial (validateLogin, Input1, Input2)


# Creating login button
loginButton = Button (console, text="Login", command=validateLogin). grid (row=4, column=0)  


console.mainloop()