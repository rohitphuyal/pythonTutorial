import csv

# Read and process the CSV
with open("students.csv", "r") as infile:
    reader = csv.reader(infile)
    rows = list(reader)

# Extract header and append 'total'
header = rows[0]
header.append("total")

# Process each student row
updated_rows = [header]
for row in rows[1:]:
    name, age = row[0], row[1]
    # Convert available marks to integers, skipping name and age
    marks = [int(m.strip()) for m in row[2:] if m.strip().isdigit()]
    total = sum(marks)
    updated_rows.append(row + [str(total)])

# Write to a new CSV file
with open("students_with_total.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(updated_rows)

# Print the result
print("Modified data with total marks:\n")
for row in updated_rows:
    print(row)
