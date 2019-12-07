class Person:
    def __init__(self, pname, page):
        self.pname = pname
        self.page = page

    def __str__(self):
        return ("이름: " + self.pname + " 나이:" + str(self.page))

    def print(self):
        print("이름: " + self.pname + " 나이:" + str(self.page))

    def getOlder(self):
        self.page += 1

