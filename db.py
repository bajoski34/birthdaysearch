import csv
no_of_person = 0
info = {

}
with open('info.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            no_of_person += 1
            info[f"person{no_of_person}"]= {'firstname':row['first_name'],'lastname': row['last_name'], 'date': row['Date']}
         

          










