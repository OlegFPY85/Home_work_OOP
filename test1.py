class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calculate_average_hw_grade(self):
        total_grade = 0
        count = 0
        for grades in self.grades.values():
            total_grade += sum(grades)
            count += len(grades)
        if count != 0:
            return round(total_grade / count, 1)
        else:
            return 0

    def __str__(self):
        return f'имя: {self.name}\nфамилия: {self.surname}\nсредняя оценка за домашние задания: {self.calculate_average_hw_grade()}\nкурсы в процессе изучения: {self.courses_in_progress}\nзавершенные курсы: {self.finished_courses}'

    def __gt__(self, other):
        avg_grade_self = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        avg_grade_other = sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values())
        return avg_grade_self > avg_grade_other

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}
        self.courses_attached = []

    def calculate_average_lectures_grade(self):
        total_grade = 0
        count = 0
        for grades in self.lecture_grades.values():
            total_grade += sum(grades)
            count += len(grades)
        if count != 0:
            return round(total_grade / count, 1)
        else:
            return 0

    def __gt__(self, other):
        avg_lecture_grade_self = sum(sum(values) for values in self.lecture_grades.values()) / sum(
            len(values) for values in self.lecture_grades.values())
        avg_lecture_grade_other = sum(sum(values) for values in other.lecture_grades.values()) / sum(
            len(values) for values in other.lecture_grades.values())
        return avg_lecture_grade_self > avg_lecture_grade_other

    def __str__(self):
        # tmp = self.calculate_average_lectures_grade()
        return f'имя: {self.name}\nфамилия: {self.surname}\nлекции по курсу:{self.courses_attached}\nсредняя оценку за лекцию:{self.calculate_average_lectures_grade()}'


class Reviewer(Mentor):
    def __init__(self, name: object, surname: object) -> object:
        super().__init__(name, surname)
        self.validating_courses = None

    def init(self, name, surname):
        super().init(name, surname)
        self.validating_courses = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.validating_courses:
            if course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course].append(grade)
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def str(self):
        return f'имя: {self.name}\nфамилия: {self.surname}'

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calculate_average_hw_grade(self):
        total_grade = 0
        count = 0
        for grades in self.grades.values():
            total_grade += sum(grades)
            count += len(grades)
        if count != 0:
            return round(total_grade / count, 1)
        else:
            return 0

    def __str__(self):
        return f'имя: {self.name}\nфамилия: {self.surname}\nсредняя оценка за домашние задания: {self.calculate_average_hw_grade()}\nкурсы в процессе изучения: {self.courses_in_progress}\nзавершенные курсы: {self.finished_courses}'

    def __gt__(self, other):
        avg_grade_self = sum(sum(values) for values in self.grades.values()) / sum(len(values) for values in self.grades.values())
        avg_grade_other = sum(sum(values) for values in other.grades.values()) / sum(len(values) for values in other.grades.values())
        return avg_grade_self > avg_grade_other

# Создание примеров студентов, лекторов и ревьюеров

student1 = Student('ruoy', 'eman', 'your_gender')
student1.courses_in_progress += ['python']
student1.finished_courses += ['введение в программирование']

student2 = Student('emord', 'nemurb', 'your_gender')
student2.courses_in_progress += ['python']
student2.finished_courses += ['git']

lecturer1 = Lecturer('some', 'buddy')
lecturer1.courses_attached += ['python']

lecturer2 = Lecturer('another', 'buddy')
lecturer2.courses_attached += ['python']

reviewer1 = Reviewer('yet', 'another')
reviewer1.validating_courses = ['python']

reviewer2 = Reviewer('one', 'more')
reviewer2.validating_courses = ['python']

# Оценки студентов и лекторов

reviewer1.rate_hw(student1, 'python', 10)
reviewer1.rate_hw(student1, 'python', 9)
reviewer2.rate_hw(student2, 'python', 9)
reviewer2.rate_hw(student2, 'python', 9)

lecturer1.lecture_grades['python'] = [9, 8, 10, 9]
lecturer2.lecture_grades['python'] = [10, 10, 9, 10, 9]

# Определение лучшего студента и лектора

best_student = student1 if student1 > student2 else student2
best_lecturer = lecturer1 if lecturer1 > lecturer2 else lecturer2

print(f'Лучший студент по курсу: \n{best_student}')
print(f'Лучший лектор по курсу: \n{best_lecturer}')