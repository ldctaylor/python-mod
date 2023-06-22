class Student():
    organisation = "She Codes"
    
    def __init__(self,name,program_attended,year):
        self.name = name
        self.program = program_attended
        self.year = year

    def __str__(self):
        return f"<Student: {self.name}, Program: {self.program}, Year: {self.year}>"

student1 = Student("Leah","Plus",2023)
student2 = Student("Blanche","Plus",2023)
student3 = Student("Another","Flash",2022)
student4 = Student("Olivia","Plus",2019)

print(f"Student 1 is named {student1.name} and attends {student1.organisation} in {student1.year}.")

print(student4)