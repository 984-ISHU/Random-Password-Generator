#import required libraries
import random 
from tkinter import *

#funtion to a generate random password
def rpg():
    global e1
    global e2
    global e3
    global e4
    
    #retrive user inputs for password composition lengths
    lower_len = int(e1.get())
    upper_len = int(e2.get())
    num_len = int(e3.get())
    sym_len = int(e4.get())
    
    #define character sets
    numbers = [chr(i) for i in range(48, 58)]

    lower_case = [chr(i) for i in range(97, 123)]

    upper_case = [chr(i) for i in range(65, 91)]

    symbols = ['@', '#', '$', '%', '"', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<', '_', "'"]
    
    #initialize an empty password 
    temporary_password = ""
    
    #generate random digits for the password
    for x in range(num_len):
        temporary_password += random.choice(numbers)
        
    #generate random lowercase letters for the password
    for x in range(lower_len):
        temporary_password += random.choice(lower_case)
        
    #generate random uppercase letters for the password
    for x in range(upper_len):
        temporary_password += random.choice(upper_case)
        
    #generate random symbols for the password
    for x in range(sym_len):
        temporary_password += random.choice(symbols)
        
    #shuffle the characteristics of the temporary password
    for x in range(lower_len + upper_len + num_len + sym_len):
        password_list = list(temporary_password)
        random.shuffle(password_list)
        
    #intitalize final password
    password = ""
    
    #build the final password from the shuffled characters
    for x in password_list:
        password += x
        
    #update the output label with the generated password
    label_output.config(text=password, bg="#DCAE96", fg="black")

#create teh main tkinter window
root = Tk()
root.configure(bg="black")
root.title("Generating Password")
root.geometry("600x600")
photo = PhotoImage(file=r"lock.png") # load an image for the button
Button(root, text="x", image=photo).pack() #create a button with an image
#empty labels for spacing
empty_label1 = Label(root, bg="black")
empty_label1.pack()

#labels and input fields for password composition lengths
label1 = Label(root, text="ENTER THE NUMBER OF LOWER CASE CHARACTERS", bg="black", fg="#DCAE96")
label1.pack()
e1 = Entry(root, width=10, bg="gray", fg="black")
e1.pack()

label2 = Label(root, text="ENTER THE NUMBER OF UPPER CASE", bg="black", fg="#DCAE96")
label2.pack()
e2 = Entry(root, width=10, bg="gray", fg="black")
e2.pack()

label3 = Label(root, text="ENTER THE NUMBER OF NUMBERS/DIGITS", bg="black", fg="#DCAE96")
label3.pack()
e3 = Entry(root, width=10, bg="gray", fg="black")
e3.pack()

label4 = Label(root, text="ENTER THE NUMBER OF SYMBOLS", bg="black", fg="#DCAE96")
label4.pack()
e4 = Entry(root, width=10, bg="gray", fg="black")
e4.pack()

#add more empty labels for spcaing
empty_label2 = Label(root, bg="black")
empty_label2.pack()

#button to generate the password, linked with the 'rpg' function
bt1 = Button(root, text="Generate Password", command=rpg, fg="black", bg="#DCAE96")
bt1.pack()

#empty label for spcaing
empty_label3 = Label(root, bg="black")
empty_label3.pack()

#label to display the generated password
label_output = Label(root, text="",  bg="black")
label_output.pack()

root.mainloop()
