#   a118_grades.py
#   This code is incomplete.
my_courses = ["English", "Math", "CS"]

print() # blank line
print("Enter your points for " + course)

points = int(input("Points -> "))

for course in my_courses:
    if (points >= 90):
        print("A")
    elif (points >= 80):
        print("B")
    elif (points >= 70):
        print("C")
    elif (points >= 60):
        print("D")
    else:
        print("F")

    redo = input("Do you need to re-do these grades? (y/n)")

redo = "y"
while (redo == "y"):
     