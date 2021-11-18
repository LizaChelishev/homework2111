class Grade():
    def __init__(self, id, subject_name, student_id, grade):
        self.id = id
        self.subject_name = subject_name
        self.student_id = student_id
        self.grade = grade

def __str__(self):
    return f'Hello student: {self.student_id}, {self.id}/t your grade in {self.subject_name} is:{self.grade}'

def __repr__(self):
    return f'Grade(id = {self.id}, ' \
           f'student_id = {self.student_id},' \
           f'subject_name = {self.subject_name})' \
           f'grade = {self.grade}'

def __eq__(self, other):
    if isinstance(other, Grade):
        return self.grade == other.grade
    elif type(other) in [str]:
        return False

def __ne__(self,other):
    return not self.__eq__(other)

def __gt__(self,other):
    if isinstance(other, Grade):
        return self.grade > other.grade
#    elif type(other) in [int, float]:
#        return self.account_id > other
#    else:
#        # throw Error
#        return False

def __lt__(self,other):
    if isinstance(other, Grade):
        return self.grade < other.grade
#    elif type(other) in [int, float]:
#        return self.account_id < other
#    else:
#        # throw Error
#        return False

def __add__(self,other):
    self.grade += other
    return self

def __sub__(self,other):
    self.grade -= other
    return self