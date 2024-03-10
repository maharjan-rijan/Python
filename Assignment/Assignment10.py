# Create a dictionary containing marks of 5 subjects: maths = 90, science = 80, english = 70, Health = 60, Social = 50
# Find the total sum using for loop
Subjects = {
    "Math" : 90, 
    "Science" : 80, 
    "English" : 70, 
    "Health" : 60, 
    "Social" : 50
}
t_marks = 0
for marks in Subjects.values():
    t_marks = t_marks + marks
print("The Total marks is", t_marks)
