import numpy

request = raw_input("Please enter the list of student names and corresponding GPAs. Hit Enter")
studentName = raw_input("Student Name [x to exit]: ")
studentGPA = float(raw_input("Student GPA: "))
highest = 0.0
lowest = 4.0


studentStats = {}

while studentName != "x":
    studentStats[studentName] = studentGPA
    studentName = raw_input("Student Name [X to exit]: ")
    if studentName == "x":
        break
    else:
        studentGPA = float(raw_input("Student GPA: "))

print "Class GPA List"
for key,value in studentStats.items():
    print key, ":", value
    if value > highest:
        highest = value
    if value < lowest:
        lowest = value

totalStats = studentStats.values()
tcount = 0

for gpa in totalStats:
    tcount = tcount + gpa


print "Average GPA: ", (tcount / len(totalStats))

print "Highest GPA: ", highest

print "Lowest GPA: " , lowest

print "Median GPA: " , numpy.median(totalStats)

