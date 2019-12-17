
while True:
    #input supplied by the user....
    given_name = input("Enter a name: ")
    
    #information of dob of  users
    info_bank = {
        "ABRAHAM OLAOBAJU": "29/05/1997",
        "ABRAHAM SMITH": "29/05/1997",
        "LOUIS BASSEY": "21/04/2000",
        "LAWRENCE BASSEY": "21/04/2000"
        
        }
    
    
    #comparing user input to the infobank
    #if not found a response is seen.
    
    
    if given_name: 
        if given_name.upper() in info_bank:
            print(info_bank.get(given_name.upper()))
        elif given_name == 'stop':
            break
        else:
            print("Could not find the individual!")
    else:
        print("Please enter your name")
        
