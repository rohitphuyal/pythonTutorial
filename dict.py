form= {
    "f_name":"Rohit",
    "l_name":"Phuyal",
    "Address":"koteshwor",
    "Age":26,
    "country":"Nepal",
}
print(form)
print(form["f_name"])
print(form.get("f_name"))
#print(form.get("area") #if not it will return error


#updating dict
form["Gender"]="Male" #it will update in the form


print(form)


"""
questions
1. empty dict
2.ask user to enter the value for username as key, for roll number as key, for marks as key
3. ask user and update any key value
4.ask user to add any key value pair
"""

fill={
    "username":input("Enter your name:"),
    "roll_number":int(input("Enter roll number:")),
    "marks":int(input("Enter marks:"))
}
print(fill)
update=input("Which key you want to update:")
fill[update]=input("Which vsalue you want to update:")
print(fill)


#update
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

#popitem
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)