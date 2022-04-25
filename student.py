class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

s1 = Student('Robin', 34, 95)
s2 = Student('Canan', 27, 90)
s3 = Student('Mehmet', 34, 90)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.students[0].name) # Robin
print(course.students[1].name) # Canan
print(course.students[2].name) # IndexError: list index out of range
