#import Python class library "json" with the keyword "import"
import json

#create the data structure dictionary using the curly braces (include 4 spaces!)
#add key:value pairs and include different data type values such as Boolean or Array
data1 = {

    'name':'Hellery Franks',
    'age':'780',
    'city':'Lost Angeles',
    'interests':['swords','dance','shoes','pastry'],
    'is_student': True

}

#Use the `with` keyword in a "with statement"
#Using "with open(file_name, 'w' as json_file)", call dump class library method: json.dump()
with open('data1.json', 'w') as json_file:
    #dump our dictionary data1 (from line 6) into the file:
    json.dump(data1,json_file,indent=4)

#print a message to show that above code has executed successfully:
print("You have successfully written to the file data1.json")
