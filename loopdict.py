thisdict={
  "name": "Rohit",
  "age":30
}
for x in thisdict:
  print(x)



  thisdict={
  "name": "Rohit",
  "age":30
}
for x in thisdict:
  print(thisdict[x])
  
 #dotvalues
  thisdict={
  "name": "Rohit",
  "age":30
}

for x in thisdict.values():
 print(x)

#dotitems
thisdict={
  "name": "Rohit",
  "age":30
}
x,y =("name", "Rohit")
("age", 30)

for k,v in thisdict.items():
  print(k,v)