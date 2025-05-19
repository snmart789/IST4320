#!/usr/bin/env python
# coding: utf-8

# In[35]:


# I will begin with a starting screen
import tkinter as tk
from tkinter import ttk # adding the necessary packages
import sqlite3 # here we will be inputing the data collected into social media database


# 1. Here are the windows
main = tk.Tk() # here it wil be the initiating the main window that user will interact with first
main.configure(bg="lightblue") # making the background of the main window blue
main.geometry("450x750") # here the size of the window when it pops open

# 2. making a combo box for the user to enter if they are a new or a returning user
new_returning = tk.StringVar()
choice = ttk.Combobox(main, width=20, textvariable = new_returning)
choice['values'] = ('Select',
                    'Returning User', # these are the option names
                    'New User')

choice.set(0) # the deault is set to 'select'
choice.pack()

def open_calc(): # 3. this function is for the main submit button to open the second window
    input_info = tk.Toplevel() # initiating the second window
    input_info.configure(bg="lightpink")
    input_info.geometry("450x750")
    begin_input = tk.Label(input_info, text="Welcome New User", 
                           font=("Arial",35,"bold"), 
                           bg="lightpink", 
                           fg="darkred") 
    
    begin_input.pack()
    
    # 4. User is entering input

    # initializing the variables that will collect user data
    user_name = tk.StringVar()  
    user_age = tk.IntVar() 
    user_accname = tk.StringVar()
    user_password = tk.StringVar()

    # 5. creating the database that will store the data
    sql_connect = sqlite3.connect('besties.db')
    cur = sql_connect.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS user_info (       
        name TEXT,
        age INTEGER,
        username TEXT,
        password TEXT
        )
    ''')
    sql_connect.commit() # creating the entity that will hold the columns name, age, username, password

    
    # database labels second page
    q_Name = tk.Label(input_info, text="What is your name?",
                  font=("Verdana",20,'bold'),
                     bg="lightpink")

    q_Age = tk.Label(input_info, text="What is your age?",
                 font=("Verdana",20,"bold"),
                    bg="lightpink")

    q_Usern = tk.Label(input_info, text="Create your username:",
                   font=("Verdana",20,"bold"),
                      bg="lightpink")

    q_Pass = tk.Label(input_info, text="Create your password:",
                  font=("Verdana",20,"bold"),
                     bg="lightpink")



    # entries where user will input their answer
    a_Name = tk.Entry(input_info,
                  textvariable = user_name,
                  font=('Verdana',15))
    a_Age = tk.Entry(input_info,
                  textvariable = user_age,
                  font=('Verdana',15))
    a_Usern = tk.Entry(input_info,
                  textvariable = user_accname,
                  font=('Verdana',15))
    a_Pass = tk.Entry(input_info,
                  textvariable = user_password,
                  font=('Verdana',15))
    # start function this will receive the user input from the entry
    def get_valuesDB():
        name = user_name.get()
        age = user_age.get()
        username = user_accname.get()
        password = user_password.get()
    
        # saving data into the BESTIES.db
        query = "INSERT INTO user_info (name, age, username, password) VALUES (?,?,?,?)"
        cur.execute(query, (name, age, username, password))
        sql_connect.commit()
        
        # clear out the inputs for new ones
        user_name.set("")
        user_age.set("")
        user_accname.set("")
        user_password.set("")
        main.destroy
    submit_inp = tk.Button(input_info,
                           text="SUBMIT",
                           font=('verdana',15),
                           command=get_valuesDB)
        

# here they will be executed
    q_Name.pack()
    a_Name.pack()

    q_Age.pack()
    a_Age.pack()

    q_Usern.pack()
    a_Usern.pack()

    q_Pass.pack()
    a_Pass.pack()
    submit_inp.pack()

    #this button will have a close button where user can exit the app when they are done/cancel
    closeapp = tk.Button(input_info, 
                         text="CLOSE", 
                         command=input_info.destroy) 
    closeapp.pack()
    # here I have to return the SQL value to be able to run it
    return sql_connect
# new holder
result = open_calc()
# 2. the labels

# main menu labels
labelWelcome = tk.Label(main, text="BESTIES", 
                        fg="darkblue", bg="lightblue", 
                        font=("Arial",45,"bold"),
                        padx=10, pady=5, 
                        justify=tk.CENTER)
labelBegin = tk.Label(main, text="Select an option\n to begin :)", 
                      fg="darkblue", 
                      bg="lightblue", 
                      font=("Arial",20,"bold"))

photoMain = tk.PhotoImage(file="Kirby_Nintendo.png") # every few runs the images will have issues and I am not sure why
labelPhoto = tk.Label(main, image=photoMain)



# 3. the buttons

# from the main page, this will redirect the user when they are ready
beginButton = tk.Button(main, text="SUBMIT", 
                        font=("Arial",20), 
                        fg="darkblue", 
                        bg="lightblue",
                        command=open_calc)



# 4. Execution and Display
labelWelcome.pack()
labelBegin.pack()
labelPhoto.pack()

beginButton.pack(side="bottom")




main.mainloop()



# In[33]:


# testing the database have to use the new variable result to retrieve the database
import pandas as pd
pd.read_sql_query('''
    SELECT * FROM user_info;
    ''', result)


# In[ ]:




