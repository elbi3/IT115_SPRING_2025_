#import class library "json" with the keyword "import"
import json

#create the data structure dictionary using the curly braces (4 spaces!)
#add key:value pairs and include different data type values such as Boolean or Array
data1 = {

    'name':'Hellery Franks',
    'age':'780',
    'city':'Lost Angeles',
    'interests':['swords','dance','shoes','pastry'],
    'is_student': True

}

#use with keyword in with statement
#with open(Name, 'w' as json_file) use dump class library method: json.dump()
with open('data1.json', 'w') as json_file:
    #dump our dictionary data1 into the file
    json.dump(data1,json_file,indent=4)

#print a message to show that above code has executed successfully:
print("You have successfully written to the file data1.json")