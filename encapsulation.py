class Student():
    def __init__(self, score):
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, new_score):
        if 0<=new_score<=700:
            self.__score = new_score
        else:
            print("invalid score")
S1 = Student(500)
print(Student.score())