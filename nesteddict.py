#The given "1,2,3" are the roll numbers which is the unique key to find the students details

students={
1: {
    "Name": "ram xyz",
    "marks":{
        "maths":80,
        "science":14,
        "english":50,
        "nepali":32
    },
    "address": "KTM",
    "contact_number": [1111112134,1245834697]
},
2: {
    "Name": "shyam xyz",
    "marks":[51,41,31,57,52],
    "address": "Lalitpur",
    "contact_number": [1111002134,1288834697]
},
3: {
    "Name": "hari xyz",
    "marks":[20,30,25,70,85],
    "address": "Bhaktapur",
    "contact_number": [9771111213,1375834555]
}

}

#excess
#print(students[1]["Name"])

#printing all names using loops
for student_id in students:
    print(students[student_id]["Name"])

#finding lowest and highest marks
max_marks = 0
max_key = ""
xyz = students[1]["marks"]

for k, v in xyz.items():
    if v > max_marks:
        max_marks = v
        max_key = k

print(max_marks)
print(max_key)
        




        


        
