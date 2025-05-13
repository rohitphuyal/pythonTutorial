import csv
# file_path="C:/Users/Rohit/Desktop/Basic/data.csv"

# #reading csv file using csv.reader
# with open (file_path, mode="r") as file:
#     csv_reader=csv.reader(file)
#     header=next(csv_reader) #read the header row
#     for row in csv_reader:
#         print(row[0]) 

# #example
# data=[
#     ['Alice',30,'London'],
#     ['Bob',25,'USA'],
#     ['Charlie',28,'Berlin']
# ]
# #writing data to CSV file usiing csv.writer
# file_path="output.csv"
# with open(file_path, mode="w", newline='') as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(["Name", "Age", "City"]) #write header
#     for row in data:
#         csv_writer.writerow(row)


# #appending data to CSV file usiing csv.writer in exixting data.csv file
# file_path="data.csv"
# with open(file_path, mode="a", newline='') as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(["Name", "Age", "City"]) #write header
#     for row in data:
#         csv_writer.writerow(row)


# #Reading CSV file using DictReader
# file_path="data.csv"
# with open(file_path, mode="r") as file:
#     csv_reader=csv.DictReader(file)
#     for row in csv_reader:
#         print(row)
#         print(row["Name"], row["Age"])

#Example data to write to csv

data=[
    {"Name":'Alice',"Age":30,"City":'London'},
    {"Name":'Raj',"Age":31,"City":'Nepal'}
]
#writing data to CSV file usiing csv.writer
file_path="output.csv"
fieldnames=["Name", "Age", "City"]
with open(file_path, mode="w", newline='') as file:
    writer=csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader() #write header row
    for row in data:
        print(row)
        writer.writerow(row)  