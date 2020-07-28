class Student:
    
    def __init__(self, name, gender, grades):
        self.name = name
        self.gender = gender
        self.grades = [grades]
        
    def avg(self):
        return sum(self.grades)/len(self.grades)
    
    def add(self, grade):
        self.grades.append(grade)
        
    def fcount(self):
        count = 0
        for grad in self.grades:
            if grad < 60:
                count += 1
        return count

stu1 = Student('Amy', 'F', 60)
stu2 = Student('Bob', 'M', 50)
print(stu1.name, stu1.gender, stu1.grades)
print(stu1.avg())
print(stu1.fcount())
print(stu2.name, stu2.gender, stu2.grades)
print(stu2.avg())
print(stu2.fcount())
