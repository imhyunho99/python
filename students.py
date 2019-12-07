import person
class Student(person.Person):
    def __init__(self,pname,page,pgrade,pnum):
        super().__init__(pname,page)
        self.pgrade = pgrade
        self.pnum = pnum

    def __str__(self):
        return ("이름: " + self.pname + " 나이:" + str(self.page) + " 학년: " + str(self.pgrade) + " 학번: " + str(self.pnum))

    def print(self):
        print("이름: " + self.pname + " 나이:" + str(self.page) + " 학년: " + str(self.pgrade) + " 학번: " + str(self.pnum))

    def upGrade(self):
        self.pgrade += 1
