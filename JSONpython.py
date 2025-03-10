#import the json library
import json

#create a dictionary with 4 space indentions
data1 = {
    'name':'Josh Cep',
    'age':'33',
    'city':'Silverdale, WA',
    'interests':['Video Games', 'Anime','Family Trips'],
    'is_student': True
}

#create the json files that hold the dictionaries made
with open('data1.json','w') as json_file:
    
    #use the .dump to put the data from 'data1' into the file
    json.dump(data1, json_file, indent=4)

#confirmation message
print("You have successfully written to data1.json")