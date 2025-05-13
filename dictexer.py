student={
    "name":"Ram xyz",
    "roll_number":12,
    "marks":[50,40,30,80],
    "address":"Ktm",
    "contant_number":[9860062006,9849441355]
}
name=student["name"]
name_in_list=name.split(" ") #[Ram, xyz]
firstname=name_in_list[0]
lastname=name_in_list[1]
print(name)
print(name_in_list)
print(firstname)
print(lastname)

marks_obtained=student["marks"]
total_marks=sum(marks_obtained)
student["total_marks_obtained"]=total_marks
print(student)
'''
contacts=student["contact_number"] #[9860062006,9849441355]
for x in contacts:
    print(x)
    if len(str(x))==10:
        print("Number has 10 digit")
    else:
        print("invalid Number")
'''

#ask from user
student_info={
    "username":input("Enter your full name:"),
    "age":int(input("Enter your age:")),
    "rollnumber":int(input("Enter your roll number:")),
    "marks":int(input("Enter your marks:")),
}
fullname=student_info["username"]
print(fullname) 