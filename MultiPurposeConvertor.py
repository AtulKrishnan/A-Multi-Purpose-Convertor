#As we will be using GUI we import the module Tkinter
from tkinter import *

#Creating a window
root = Tk()

#Label is used to add statements on the window
#Color is added to the background and foreground using bg and fg
greet = Label(root, text = "Welcome to convertor",bg="black",fg="cyan")
#Unless we pack the Label function, it will not get embedded on the output screem
greet.pack()
greet1 = Label(root, text = "What kind of conversion would you like to do?",bg="black",fg="cyan")
greet1.pack()
#This command adds color to the window
root['bg']='tomato'

#This is the function main
def main():

    #All the temperature related calculations take place in this function
    def Temp():

        Ans = ""
        A1 = 0
        #This step is to make calculations easier
        #The value needs to be accessed using .get() function
        e_vari = e_var.get()                                                                

        #Variable2.get() stores the value of the first drop down menu 
        #Variable3.get() stores the value of the second drop down menu
        if Variable2.get() == Variable3.get():                                                  
            Ans = e_vari
        elif Variable2.get() == "Celsius" and Variable3.get() == "Farenheit":
            Ans = (e_vari*(9/5)) + 32
        elif Variable2.get() == "Farenheit" and Variable3.get() == "Celsius":
            Ans = (e_vari - 32)*(5/9)
        elif Variable2.get() == "Celsius" and Variable3.get() == "Kelvin":
            Ans = e_vari + 273
        elif Variable2.get() == "Kelvin" and Variable3.get() == "Celsius":
            Ans = e_vari - 273
        elif Variable2.get() == "Farenheit" and Variable3.get() == "Kelvin":
            A1 = (e_vari - 32)*(5/9)
            Ans = A1 + 273
        elif Variable2.get() == "Kelvin" and Variable3.get() == "Farenheit":
            A1 = e_vari - 273
            Ans = (A1*(9/5)) + 32
        #The answer after calculation gets displayed here
        Lb1 = Label(root1, text = Ans, bg="black",fg="cyan").pack()

    #All conversions and calculations related to currency happens here
    def Curr():

        Ans = ""
        A1 = 0
        #This step is to make calculations easier
        #The value needs to be accessed using .get() function
        e_vari = e_var.get()                                                                

        if e_vari >= 0:
            #Variable2.get() stores the value of the first drop down menu 
            #Variable3.get() stores the value of the second drop down menu
            if Variable2.get() == Variable3.get():                                                  
                Ans = e_vari
            elif Variable2.get() == "Rupees" and Variable3.get() == "US Dollar":
                Ans = (e_vari*(0.014))
            elif Variable2.get() == "Rupees" and Variable3.get() == "Euros":
                Ans = (e_vari)*(0.011)
            elif Variable2.get() == "Rupees" and Variable3.get() == "Japanese Yen":
                Ans = (e_vari*(1.47))
            elif Variable2.get() == "Rupees" and Variable3.get() == "Dhirams":
                Ans = (e_vari*(0.051))
            elif Variable2.get() == "US Dollar" and Variable3.get() == "Rupees":
                Ans = (e_vari*(72.44))
            elif Variable2.get() == "US Dollar" and Variable3.get() == "Euros":
                Ans = (e_vari*(0.82))
            elif Variable2.get() == "US Dollar" and Variable3.get() == "Japanese Yen":
                Ans = (e_vari*(106.12))
            elif Variable2.get() == "US Dollar" and Variable3.get() == "Dhirams":
                Ans = (e_vari*(3.67))
            elif Variable2.get() == "Euros" and Variable3.get() == "Rupees":
                Ans = (e_vari*(88.50))
            elif Variable2.get() == "Euros" and Variable3.get() == "US Dollar":
                Ans = (e_vari*(1.22))
            elif Variable2.get() == "Euros" and Variable3.get() == "Japanese Yen":
                Ans = (e_vari*(129.62))
            elif Variable2.get() == "Euros" and Variable3.get() == "Dhirams":
                Ans = (e_vari*(4.49))
            elif Variable2.get() == "Japanese Yen" and Variable3.get() == "Rupees":
                Ans = (e_vari*(0.68))
            elif Variable2.get() == "Japanese Yen" and Variable3.get() == "US Dollar":
                Ans = (e_vari*(0.0094))
            elif Variable2.get() == "Japanese Yen" and Variable3.get() == "Euros":
                Ans = (e_vari*(0.0077))
            elif Variable2.get() == "Japanese Yen" and Variable3.get() == "Dhirams":
                Ans = (e_vari*(0.035))
            elif Variable2.get() == "Dhirams" and Variable3.get() == "Rupees":
                Ans = (e_vari*(19.72))
            elif Variable2.get() == "Dhirams" and Variable3.get() == "US Dollar":
                Ans = (e_vari*(0.27))
            elif Variable2.get() == "Dhirams" and Variable3.get() == "Euros":
                Ans = (e_vari*(0.22))
            elif Variable2.get() == "Dhirams" and Variable3.get() == "Japanese Yen":
                Ans = (e_vari*(28.87))

            #The answer after calculation gets displayed here
            Lb1 = Label(root1, text = Ans,bg="black",fg="cyan").pack()

        else:
            Lb9 = Label(root1, text = "Enter a valid number",bg="black",fg="cyan")
 

    #After selecting which unit we want to convert, the button redirects the program here
    def units():

        #All length related conversions and calculations take place in this module
        def Len():

            Ans = ""
            #This step is to make calculations easier
            #The value needs to be accessed using .get() function
            e_vari = e_va.get()

            if e_vari >= 0:
                #Variable2.get() stores the value of the first drop down menu 
                #Variable3.get() stores the value of the second drop down menu
                if Variable2.get() == Variable3.get(): 
                  Ans = e_vari
                elif Variable2.get() == "Meter" and Variable3.get() == "Feet":
                  Ans = (e_vari*(3.28084))
                elif Variable2.get() == "Meter" and Variable3.get() == "Kilometer":
                  Ans = (e_vari)*(0.001)
                elif Variable2.get() == "Meter" and Variable3.get() == "Centimeter":
                  Ans = (e_vari*(100))
                elif Variable2.get() == "Meter" and Variable3.get() == "Inches":
                  Ans = (e_vari*(39.3701))
                elif Variable2.get() == "Feet" and Variable3.get() == "Meter":
                  Ans = (e_vari*(0.3048))
                elif Variable2.get() == "Feet" and Variable3.get() == "Kilometer":
                  Ans = (e_vari*(0.0003048))
                elif Variable2.get() == "Feet" and Variable3.get() == "Centimeter":
                  Ans = (e_vari*(30.48))
                elif Variable2.get() == "Feet" and Variable3.get() == "Inches":
                  Ans = (e_vari*(12))
                elif Variable2.get() == "Kilometer" and Variable3.get() == "Meter":
                  Ans = (e_vari*(1000))
                elif Variable2.get() == "Kilometer" and Variable3.get() == "Feet":
                  Ans = (e_vari*(3280.84))
                elif Variable2.get() == "Kilometer" and Variable3.get() == "Centimeter":
                  Ans = (e_vari*(100000))
                elif Variable2.get() == "Kilometer" and Variable3.get() == "Inches":
                  Ans = (e_vari*(39370.1))
                elif Variable2.get() == "Centimeter" and Variable3.get() == "Meter":
                  Ans = (e_vari*(0.01))
                elif Variable2.get() == "Centimeter" and Variable3.get() == "Kilometer":
                  Ans = (e_vari*(0.00001))
                elif Variable2.get() == "Centimeter" and Variable3.get() == "Feet":
                  Ans = (e_vari*(0.0328084))
                elif Variable2.get() == "Centimeter" and Variable3.get() == "Inches":
                  Ans = (e_vari*(0.393701))
                elif Variable2.get() == "Inches" and Variable3.get() == "Meter":
                  Ans = (e_vari*(0.0254))
                elif Variable2.get() == "Inches" and Variable3.get() == "Kilometer":
                  Ans = (e_vari*(2.54000508))
                elif Variable2.get() == "Inches" and Variable3.get() == "Feet":
                  Ans = (e_vari*(0.0833333))
                elif Variable2.get() == "Inches" and Variable3.get() == "Centimeter":
                  Ans = (e_vari*(2.54))

                #The answer after calculation gets displayed here
                Lb1 = Label(root2, text = Ans,bg="black",fg="cyan").pack()

            else:
                Lb9 = Label(root1, text = "Enter a valid number",bg="black",fg="cyan")

        #All mass related calculations and conversions take place in this module
        def mass():
            Ans = ""
            #This step is to make calculations easier
            #The value needs to be accessed using .get() function
            e_vari = e_va.get() 

            if e_vari >= 0:
                #Variable2.get() stores the value of the first drop down menu 
                #Variable3.get() stores the value of the second drop down menu
                if Variable2.get() == Variable3.get(): 
                   Ans = e_vari
                elif Variable2.get() == "Grams" and Variable3.get() == "Kilograms":
                   Ans = (e_vari*(0.001))
                elif Variable2.get() == "Grams" and Variable3.get() == "Pounds":
                   Ans = (e_vari*(0.00220462))
                elif Variable2.get() == "Pounds" and Variable3.get() == "Kilograms":
                   Ans = (e_vari*(0.453592))
                elif Variable2.get() == "Pounds" and Variable3.get() == "Grams":
                   Ans = (e_vari*(453.592))
                elif Variable2.get() == "Kilograms" and Variable3.get() == "Pounds":
                   Ans = (e_vari*(2.20462))
                elif Variable2.get() == "Kilograms" and Variable3.get() == "Grams":
                   Ans = (e_vari*(1000))

                #The answer after calculation gets displayed here
                Lb1 = Label(root2, text = Ans,bg="black",fg="cyan").pack()
            else:
                Lb9 = Label(root1, text = "Enter a valid number",bg="black",fg="cyan")

        #All volume related conversions and calculations take place in this module
        def Vol():
            Ans = ""
            #This step is to make calculations easier
            #The value needs to be accessed using .get() function
            e_vari = e_va.get() 

            if e_vari >= 0:
                #Variable2.get() stores the value of the first drop down menu 
                #Variable3.get() stores the value of the second drop down menu
                if Variable2.get() == Variable3.get(): 
                   Ans = e_vari
                elif Variable2.get() == "Gallons" and Variable3.get() == "Kilolitres":
                   Ans = (e_vari*(0.00378541))
                elif Variable2.get() == "Gallons" and Variable3.get() == "Litres":
                   Ans = (e_vari*(3.78541))
                elif Variable2.get() == "Litres" and Variable3.get() == "Kilolitres":
                   Ans = (e_vari*(0.001))
                elif Variable2.get() == "Litres" and Variable3.get() == "Gallons":
                   Ans = (e_vari*(0.264172))
                elif Variable2.get() == "Kilolitres" and Variable3.get() == "Litres":
                   Ans = (e_vari*(1000))
                elif Variable2.get() == "Kilolitres" and Variable3.get() == "Gallons":
                   Ans = (e_vari*(264.172))

                #The answer after calculation gets displayed here
                Lb1 = Label(root2, text = Ans,bg="black",fg="cyan").pack()

            else:
                Lb9 = Label(root1, text = "Enter a valid number",bg="black",fg="cyan")

        #When the user asks for a particular unit conversion a third window is created for the ease of access
        #This window presents the options from which the user can convert any value
        root2 = Tk()
        root2['bg']='black'

        #Error handling block for the window root2
        def root2_report_callback_exception(self, exc, val):
            Lb8 = Label(root2, text = "Enter a valid number",bg="black",fg="cyan").pack()

        root2.report_callback_exception = root2_report_callback_exception

        #The program enters this set of statements if the user wanted a length convertor 
        if Variable4.get() == "Length":

            greet2 = Label(root2, text = "Welcome to Length converter",bg="black",fg="cyan").pack()

            #The list of options for the drop down menu
            T_Options1 = ["Meter", "Centimeter", "Kilometer", "Feet", "Inches"]
            T_Options2 = ["Meter", "Centimeter", "Kilometer", "Feet", "Inches"]

            #We are defining the data type of the value we select in the drop down menu
            Variable2 = StringVar(root2)
            Variable2.set(T_Options1[0])

            Variable3 = StringVar(root2)
            Variable3.set(T_Options2[0])

            #The user can choose the type he wants the conversion from
            Lb2 = Label(root2, text = "Conversion from",bg="black",fg="cyan").pack()
            T_drop1 = OptionMenu( root2, Variable2, *T_Options1)
            T_drop1.config(bg = "black", fg = "cyan")
            T_drop1.pack()

            #The user can choose the type he wants to convert to
            Lb4 = Label(root2, text = "Conversion to",bg="black",fg="cyan").pack()
            T_drop2 = OptionMenu( root2, Variable3, *T_Options2)
            T_drop2.config(bg = "black", fg = "cyan")
            T_drop2.pack()

            #We are defining the datatype of the value we enter in the textbox
            Lb3 = Label(root2, text = "Enter Length",bg="black",fg="cyan").pack()
            e_va = IntVar(root2) 
            e_va.set(0)

            #This is the command to create the textbox
            e = Entry(root2, width = 50, textvariable = e_va).pack()

            #This button redirects the program to the function Len
            bt2 = Button(root2, text = "Go", command = Len,bg="black",fg="cyan").pack() 

        #The program enters this set of statements if the user wanted a mass convertor
        elif Variable4.get() == "Mass":

            greet2 = Label(root2, text = "Welcome to Mass converter",bg="black",fg="cyan").pack()

            #The list of options for the drop down menu
            T_Options1 = ["Grams", "Kilograms", "Pounds"]
            T_Options2 = ["Grams", "Kilograms", "Pounds"]

            #We are defining the datatype of the value we select in the drop down menu
            Variable2 = StringVar(root2)
            Variable2.set(T_Options1[0])

            Variable3 = StringVar(root2)
            Variable3.set(T_Options2[0])

            #The user can choose the type he wants the conversion from
            Lb2 = Label(root2, text = "Conversion from",bg="black",fg="cyan").pack()
            T_drop1 = OptionMenu( root2, Variable2, *T_Options1)
            T_drop1.config(bg = "black", fg = "cyan")
            T_drop1.pack()

            #The user can choose the type he wants to convert to
            Lb4 = Label(root2, text = "Conversion to",bg="black",fg="cyan").pack()
            T_drop2 = OptionMenu( root2, Variable3, *T_Options2)
            T_drop2.config(bg = "black", fg = "cyan")
            T_drop2.pack()

            #We are defining the datatype of the value we enter into the textbox
            Lb3 = Label(root2, text = "Enter the value of Weight",bg="black",fg="cyan").pack()
            e_va = IntVar(root2) 
            e_va.set(0) 

            #The user can enter the value in this textbox
            e = Entry(root2, width = 50, textvariable = e_va).pack()

            #This button redirects the program to the function mass
            bt2 = Button(root2, text = "Go", command = mass,bg="black",fg="cyan").pack()

        #The program enters this set of statements if the user wanted a volume convertor
        elif Variable4.get() == "Volume":

            greet2 = Label(root2, text = "Welcome to Volume converter",bg="black",fg="cyan").pack()

            #The list of options for the drop down menu
            T_Options1 = ["Gallons", "Kilolitres", "Litres"]
            T_Options2 = ["Gallons", "Kiloliters", "Litres"]

            #The datatype of the element we select in the drop down menu
            Variable2 = StringVar(root2)
            Variable2.set(T_Options1[0])

            Variable3 = StringVar(root2)
            Variable3.set(T_Options2[0])

            #The user can choose the type he wants the conversion from
            Lb2 = Label(root2, text = "Conversion from",bg="black",fg="cyan").pack()
            T_drop1 = OptionMenu( root2, Variable2, *T_Options1)
            T_drop1.config(bg = "black", fg = "cyan")
            T_drop1.pack()

            #The user can choose the type he wants to convert to
            Lb4 = Label(root2, text = "Conversion to",bg="black",fg="cyan").pack()
            T_drop2 = OptionMenu( root2, Variable3, *T_Options2)
            T_drop2.config(bg = "black", fg = "cyan")
            T_drop2.pack()

            #We are defining the datatype for the value the user enters in the textbox
            Lb3 = Label(root2, text = "Enter the value of volume",bg="black",fg="cyan").pack()
            e_va = IntVar(root2) 
            e_va.set(0) 

            #The user can input the value here
            e = Entry(root2, width = 50, textvariable = e_va).pack()

            #This button redirects the program to function Vol
            bt2 = Button(root2, text = "Go", command = Vol,bg="black",fg="cyan").pack()

        #We loop the entire program so that we can use it multiple times
        root2.mainloop()

    #We are creating another window for ease of access
    #As a result all 3 types of conversions could be done side by side without affecting each other
    root1 = Tk()
    root1['bg']='black'

    #Error handling block for root1
    def root1_report_callback_exception(self, exc, val):
        Lb7 = Label(root1, text = "Enter a valid number",bg="black",fg="cyan").pack()

    root1.report_callback_exception = root1_report_callback_exception

    #Variable1 stores the value we selected in the drop down menu
    #To access the value we use the function .get()
    #The program enters this set of statements if the user asks for a temperature convertor
    if Variable1.get() == "Temperature":

       greet2 = Label(root1, text = "Welcome to temperature converter",bg="black",fg="cyan").pack()

       #The list of options for the drop down menu
       T_Options1 = ["Celsius", "Farenheit", "Kelvin"]
       T_Options2 = ["Celsius", "Farenheit", "Kelvin"]

       #We are defining the datatype of the value in the drop down menu
       Variable2 = StringVar(root1)
       Variable2.set(T_Options1[0])

       Variable3 = StringVar(root1)
       Variable3.set(T_Options2[0])

       #The user can choose the type he wants the conversion from
       Lb2 = Label(root1, text = "Conversion from",bg="black",fg="cyan").pack()
       T_drop1 = OptionMenu( root1, Variable2, *T_Options1)
       T_drop1.config(bg = "black", fg = "cyan")
       T_drop1.pack()

       #The user can choose the type he wants to convert to
       Lb4 = Label(root1, text = "Conversion to",bg="black",fg="cyan").pack()
       T_drop2 = OptionMenu( root1, Variable3, *T_Options2)
       T_drop2.config(bg = "black", fg = "cyan")
       T_drop2.pack()

       Lb3 = Label(root1, text = "Enter Temperature",bg="black",fg="cyan").pack()

       #We are defining the data type of the value to be entered in the textbox and setting it as 0
       e_var = IntVar(root1)               
       e_var.set(0)

       #This is the command to create a textbox
       #The value we enter gets stored in the variable e_var
       #The user inputs the value here
       e = Entry(root1, width = 50, textvariable = e_var).pack()

       #A button is created that directs the program to a function Temp
       bt2 = Button(root1, text = "Go", command = Temp,bg="black",fg="cyan").pack()              

    #The program enters this set of statements if the user asks for a Currency convertor
    elif Variable1.get() == "Currency":    

         greet2 = Label(root1, text = "Welcome to currency converter",bg="black",fg="cyan").pack()

         #The list of options for the drop down menu
         C_Options1 = ["Rupees", "US Dollar", "Euros","Japanese Yen","Dhirams"]
         C_Options2 = ["Rupees", "US Dollar", "Euros","Japanese Yen","Dhirams"]

         #We are defining the data type of the value we select in the drop down menu
         Variable2 = StringVar(root1)
         Variable2.set(C_Options1[0])

         Variable3 = StringVar(root1)
         Variable3.set(C_Options2[0])

         #The user can choose the type he wants the conversion from
         Lb2 = Label(root1, text = "Conversion from",bg="black",fg="cyan").pack()
         T_drop1 = OptionMenu( root1, Variable2, *C_Options1)
         T_drop1.config(bg = "black", fg = "cyan")
         T_drop1.pack()

         #The user can choose the type he wants to convert to
         Lb4 = Label(root1, text = "Conversion to",bg="black",fg="cyan").pack()
         T_drop2 = OptionMenu( root1, Variable3, *C_Options2)
         T_drop2.config(bg = "black", fg = "cyan")
         T_drop2.pack()

         Lb3 = Label(root1, text = "Enter the value of Currency",bg="black",fg="cyan").pack()

         #We are defining the datatype of the value the user should enter
         e_var = IntVar(root1)                                                
         e_var.set(0)

         #The user can enter the value here
         e = Entry(root1, width = 50, textvariable = e_var).pack()            

         #A button is created which directs the program to the function Curr
         bt2 = Button(root1, text = "Go", command = Curr,bg="black",fg="cyan").pack()

    #The program enters this set of statements if the user asks for a units convertor     
    elif Variable1.get() == "Units":
        
         greet2 = Label(root1, text = "Welcome to units converter",bg="black",fg="cyan").pack()
         greet5 = Label(root1, text = "Which kind of units would you like to convert?",bg="black",fg="cyan").pack()

         #The list of options for the drop down menu
         U_options = ["Length", "Volume", "Mass"]

         #We are defining the datatype of the value we select in the drop down menu
         Variable4 = StringVar(root1) 
         Variable4.set(U_options[0]) 

         #We are creating the drop down menu
         drop = OptionMenu(root1 , Variable4, *U_options) 
         drop.config(bg = "black", fg = "cyan")
         drop.pack()

         #We are creating a button that leads the user to a new window
         bt5 = Button(root1, text = "Go", command = units, bg="black",fg="cyan") 
         bt5.pack()

    #We loop the entire program so that we can use it multiple times
    root1.mainloop()

#The main body of the program       
options = ["Temperature", "Currency", "Units"]
#We are defining the data type of the drop down menu and whatever we select in it gets stored in Variable1
Variable1 = StringVar(root)                             
#We are setting a default value in the drop down menu
Variable1.set(options[0])                               
#This is the comand used to create a drop down menu with the list options
#*options means multiple parameters
drop = OptionMenu( root , Variable1, *options)          
drop.config(bg = "black", fg = "cyan")
drop.pack()

#This is the command to create a button in the window
#Clicking on it will redirect you to the function in it(main)
bt1 = Button(root, text = "Go", command = main,bg="black",fg="cyan")         
bt1.pack()

#We loop the entire program so that we can use it multiple times
root.mainloop()
