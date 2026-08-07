class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # INSTANCE METHOD
    def get_info(self):
        return f"My name is:{self.name}, and GPA is: {self.gpa}"

    # STATIC METHOD
    @staticmethod
    def is_student(student):
        is_study = [ "4th", "5th", "10th"]
        return student in is_study

    # CLASS METHOD
    @classmethod
    def get_count(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Total number of students in the class: {cls.count}"

s1 = Student("John", 6.7)
s2 = Student("Michael", 7.2)
s3 = Student("James", 7.5)
s4 = Student("Rob", 6.5)


print(Student.is_student("4th"))
print(s1.get_info())
print(s2.get_info())
print(s3.get_info())
print(s4.get_info())
print(f"{Student.is_student(s1)} :{Student.is_student(s2)} :{Student.is_student(s3)} :{Student.is_student(s4)}")
print(Student.get_count())


