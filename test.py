from tkinter import *
from progress import*


def the_search(root,init):
    
    global q_screen
    root.geometry("500x400")
    root.title("Search option")

    q_screen=Frame(root)
    text_S = Label(q_screen, text="Search using firstname and lastname :", fg="white", bg="blue", font=("arial",16,"bold"))
    text_S.pack(fill=BOTH)

    button1 = Button(q_screen,text="Yes",fg='white',bg='green',relief='raised',font=("arial",12,"bold"), command=yes)
    button1.pack(pady=20)
    
    
    
    button1 = Button(q_screen,text="No",fg='white',bg='red',relief='raised',font=("arial",12,"bold"), command=no)
    button1.pack(pady=20)



    q_screen.pack()
    
    root.mainloop()


        
        
def yes():
    init = "Y"
    option = "Y"

    progress(init, option)
def no():
    init = "N"
    option = "N"
    progress(init,option)
    exit()




