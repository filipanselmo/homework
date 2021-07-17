class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self,lecturer,course,grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'

    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 2)


    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'\
              f' Средняя оценка за ДЗ: {self.get_avg_grade() :.2f} \n'\
              f'Курсы в процессе изучения: {self.courses_in_progress[]} \n'\
              f' Изученные курсы: {self.finished_courses[]} \n'\
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}')
            return  compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades =[]

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'\
              f' Средняя оценка за ДЗ: {sum(self.grades) / len(self.grades)} \n'
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            compare = sum(self.grades) / len(self.grades) < sum(other_lecturer.grades) / len(other_lecturer.grades)
            if compare:
                print(f'{self.name} {self.surname} учит хуже, чем {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(f'{other_lecturer.name} {other_lecturer.surname} учит хуже, чем {self.name} {self.surname}')
            return  compare

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \n'\
              f'Фамилия: {self.surname} \n'\
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Git']

next_student = Student('Some', 'Name', 'm)
next_student.courses_in_progress += ['Python']
next_student.finished_courses += ['Git']

cool_reviewer = Reviewer('Some', 'Name')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)


cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)