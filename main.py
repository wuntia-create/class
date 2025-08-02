class Student: 
    def __init__(self):
         print("Student class is now active.")
         self.name = ""
         self.age = 0
         self.grade = ""
    def get_details(self):
        self.name = input("Enter student name:")
        self.age = int(input("Enter student age:"))
        self.grade = input("Enter student grade")
    def display_details(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)
student1 = Student()
student1.get_details()
student1.display_details()