#Write a Python program that reads a CSV file containing student grades, 
#calculates their average score, and writes the average to a new file.

with open("grades.csv","r") as f:
    grades = f.readlines()

averages = list()
for line in grades[1:]:
    columns = line.replace("\n","").split(";")
    names = columns[0]
    sum_grade = 0
    for grade in columns[1:]:
        sum_grade += int(grade)
    averages.append([names, sum_grade/(len(columns)-1)])

csv_output = grades[0].replace("\n","")
for student in averages:
    csv_output += "\n" + student[0] + ";" + str(student[1])

with open("Averages.csv", "w") as f:
    f.write(csv_output)