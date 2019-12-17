import datetime
from tkinter import *
from test import *



def main_account_screen():
    global root
    root = Tk()
    global main_screen
    root.geometry("500x400")
    root.title("Birthday Search")

    main_screen=Frame(root)
    start_s = Label(main_screen, text="Reveal your Birthday", fg='white',bg='red', font=("arial",16,"bold"))
    start_s.pack(fill=BOTH)
       
    
        
    button1 = Button(main_screen,text="Start Search",fg='white',bg='green',relief='raised',font=("arial",12,"bold"), command=start1)
    button1.pack(pady=20)
    
    
    
    button1 = Button(main_screen,text="Exit",fg='white',bg='red',relief='raised',font=("arial",12,"bold"), command=exit1)
    button1.pack(pady=20)

    

    main_screen.pack()
    
    
    root.mainloop()  


def start1():
    #learning for the task...
    main_screen.pack_forget()
    global init
    
    init = "y"
    the_search(root,init)
    

def exit1():
    global init
    init = "n"
    the_search(init, root)
    exit()



main_account_screen()



















     


