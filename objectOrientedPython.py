class Student():
    university = "hawassa university"
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def displayInfo(self):
        print(self.name)
        print(self.score)

    def updateScore(self, newScore):
        self.score = newScore
        print("update successful!!!")
        self.displayInfo()

    @classmethod
    def change_university(cls, new_name):
        Student.university = new_name

    @staticmethod
    def is_qualified(score):
        return score >= 400

S1 = Student("kidus", 450)
S2 = Student("yabsira", 400)
S1.displayInfo()
S1.updateScore(600)
Student.change_university("Addis Ababa University")
print(Student.university)
print(Student.is_qualified(500))
