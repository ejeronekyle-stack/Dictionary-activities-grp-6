# Activity 1: Fill in the Blanks
student = {
    "name": "Jerone",
    "age": 20,
    "course": "IT"
}
print("Activity 1:", student["name"]) 

# Activity 2: Add and Update
student = {"name": "Jerone", "age": 19}
student["grade"] = 95     
student["age"] = 20       
print("Activity 2:", student)

# Activity 3: Loop Through Dictionary
car = {"brand": "BMW", "model": "Z4", "year": 2024}
print("Activity 3:")
for key, value in car.items():
    print(key, ":", value)

# Activity 4 (Challenge): Mini Phonebook 
phonebook = {
   "Cedric": "09162173629",
    "Marc": "09519526826",
    "Charlz": "09939025809"
}

print("Activity 4 - Mini Phonebook")
name = input("Enter a name: ").strip()  
name_lower = name.lower()               

phonebook_lower = {key.lower(): value for key, value in phonebook.items()}

if name_lower in phonebook_lower:
    print("Number:", phonebook_lower[name_lower])
else:
    print("Name not found.")
