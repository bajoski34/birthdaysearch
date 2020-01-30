import datetime
import csv


#THIS PROGRAM SEARCHES FOR A USER'S BIRTHDAY AND PRINTS IT OUT.
# THE USER IS ABLE TO DO A FULLNAME SEARCH THAT REQUIRES BOTH THE FIRST AND LAST NAME
# THE USER IS ALSO ALLOWED TO DO AN ANOYNMOUS SEARCH EITHER BY TYPING A LETTER OR FIRSTNAME OR LASTNAME


init = input("Start search(Y/N): ").lower()
while init != "n":
    option = input("Search using firstname and lastname(Y/N/END): ").upper()
    global firstname, lastname, name, counter1, counter2
    counter1 = 0
    counter2 = 0
    if option ==  "Y":#search using firstname and lastname
        name = ""
        
        firstname = input("enter your firstname: ").upper()
        lastname =  input("enter your lastname: ").upper()
        
    elif option == "N": #search using any name
        firstname = ""
        lastname = ""
        name = input("Enter your name: ").upper()
        
        
    elif option == "END": #quit search
        break
    else: #invalid search parameter
        print("Enter an option!")
        break
        
        
    
    
    # a substitute to this would be to use a csv
    # info = {
    #     "person1":{"firstname":"ABRAHAM","lastname":"OLAOBAJU","date": "29/05/1997"},
    #     "person2":{"firstname":"JOHN","lastname":"DOE","date": "29/06/1985"},
    #     "person3":{"firstname":"KATTY","lastname":"HALL","date": "29/06/1996"},
    #     "person4":{"firstname":"ABRAHAM","lastname":"SMITH","date": "29/05/1967"},
    #     "person5":{"firstname":"JUDAH","lastname":"OLAOBAJU","date": "01/08/2001"},
    #     "person6":{"firstname":"CHRIS","lastname":"OPARA","date": "01/08/2002"},
    #     "person7":{"firstname":"SABASTINE","lastname":"NWANCHUKU","date": "01/08/2003"},
    #     "person8":{"firstname":"DIVINE","lastname":"NWANCHUKU","date": "01/08/2004"},
    #     "person9":{"firstname":"SAVICTOR","lastname":"ADEMOLU","date": "01/08/2005"},
    #     "person10":{"firstname":"BUCHI","lastname":"ORIAJAKU","date": "04/02/2019"}

    # }
    no_of_person = 0
    info = {
    }
    with open('info.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                no_of_person += 1
                info[f"person{no_of_person}"]= {'firstname':row['first_name'],'lastname': row['last_name'], 'date': row['Date']}
  


    

    for n in range(1,len(info)+1):
        if firstname != "" and lastname != "" and name == "":
            if firstname in info[f"person{n}"]["firstname"] and lastname in info[f"person{n}"]["lastname"]:
                
                print("Date of Birth: "+info[f"person{n}"]["date"])
                if info[f"person{n}"]["date"] != '':
                    counter1 = counter1 + 1
                else:
                    counter1 = 0
                break
        elif firstname == "" and lastname == "" and name == "":
            print("Enter firstname and lastname to begin search")
            counter1 = 88
            counter2 = 88
            break       
        
        else:
            if name in info[f"person{n}"]["firstname"] or name in info[f"person{n}"]["lastname"]:

                print(info[f"person{n}"]["firstname"]+" "+info[f"person{n}"]["lastname"] + ":" + info[f"person{n}"]["date"]+ f" (record {n})")

                if info[f"person{n}"]["firstname"] != '' and info[f"person{n}"]["lastname"] != '':
                    counter2 = counter2 + 1
                else:
                    counter2 = 0
                
                
    if counter1 == 0 and name == "":
        print(f"No result for {firstname} {lastname}")
        
    if counter2 == 0 and firstname == "" and lastname == "":
        print(f"No result found for {name}")
    
        


              
                 

             
                     



     


