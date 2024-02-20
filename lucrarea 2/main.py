from datetime import date

class StudyField:
    MECHANICAL_ENGINEERING = "MECHANICAL_ENGINEERING"
    SOFTWARE_ENGINEERING = "SOFTWARE_ENGINEERING"
    FOOD_TECHNOLOGY = "FOOD_TECHNOLOGY"
    URBANISM_ARCHITECTURE = "URBANISM_ARCHITECTURE"
    VETERINARY_MEDICINE = "VETERINARY_MEDICINE"

class Student:
    def __init__(self, first_name, last_name, email, faculty, graduated=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.faculty = faculty
        self.graduated = graduated

    def is_graduated(self):
        return self.graduated

class Faculty:
    faculties = []

    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.study_field = study_field
        self.students = []
        Faculty.faculties.append(self)

    @classmethod
    def get_faculty_by_abbreviation(cls, abbreviation):
        return next((faculty for faculty in cls.faculties if faculty.abbreviation == abbreviation), None)

    @classmethod
    def display_student_faculty(cls, email):
        student = next((student for faculty in cls.faculties for student in faculty.students if student.email == email), None)
        if student:
            print(f"{student.first_name} {student.last_name} belongs to the {student.faculty.name} faculty.")
        else:
            print("Student not found.")

    @classmethod
    def display_all_faculties(cls):
        print("Here are all the faculties:")
        for faculty in cls.faculties:
            print(f"Name: {faculty.name}, Abbreviation: {faculty.abbreviation}, Study Field: {faculty.study_field}")

    @classmethod
    def display_all_faculties_of_a_field(cls, study_field):
        print(f"Here are all the faculties belonging to {study_field}")
        for faculty in cls.faculties:
            if faculty.study_field == study_field:
                print(faculty.name)

    def create_student(self, student):
        self.students.append(student)
        print(f"{student.first_name} {student.last_name} was added to the student list")
        student.graduated = False
        print(student.graduated)

    @classmethod
    def graduate_student(cls, email):
        student = next((student for faculty in cls.faculties for student in faculty.students if student.email == email), None)
        if student:
            print(f"{student.first_name} {student.last_name} has graduated from: {student.faculty.name}")
            student.graduated = True
        else:
            print("Student not found.")

    @classmethod
    def display_students(cls, abbreviation, is_graduated):
        for faculty in cls.faculties:
            if faculty.abbreviation == abbreviation:
                print(f"Students {'graduated from' if is_graduated else 'enrolled in'} {faculty.name}:")
                for student in faculty.students:
                    if student.graduated == is_graduated:
                        print(f"{student.first_name} {student.last_name}")

    @classmethod
    def is_student_from_faculty(cls, abbreviation, email):
        faculty = next((faculty for faculty in cls.faculties if faculty.abbreviation == abbreviation), None)
        student = next((student for student in faculty.students if student.email == email), None)
        if student:
            print("Student belongs to faculty.")
        else:
            print("Student does not belong to faculty.")

    def get_students(self):
        return self.students

    def get_name(self):
        return self.name

    def get_abbreviation(self):
        return self.abbreviation

    def get_study_field(self):
        return self.study_field

def main():
    should_finish = False

    faculties_info = [
        ("Transport", "T", StudyField.MECHANICAL_ENGINEERING),
        ("Computer Science", "CSI", StudyField.SOFTWARE_ENGINEERING),
        ("Food and Nutrition", "FN", StudyField.FOOD_TECHNOLOGY),
        ("Urban Design", "UD", StudyField.URBANISM_ARCHITECTURE),
        ("Department of Food Safety and Public Health", "DFSPH", StudyField.VETERINARY_MEDICINE)
    ]

    faculties = [Faculty(name, abbreviation, study_field) for name, abbreviation, study_field in faculties_info]

    student_info = ("Sebastian", "Finciuc", "sebastian.finciuc@gmail.com", faculties[1], False)
    student2 = Student(*student_info)
    faculties[1].create_student(student2)

    while not should_finish:
        print("TUM Board Command Line \n" +
              "\t1. General Operations \n" +
              "\t2. Faculty Operations \n" +
              "\t3. Quit \n" +
              "Please choose one of the above options: ")
        choice = int(input())
        if choice == 1:
            print("General options: \n" +
                  "\t1. Create a new faculty\n" +
                  "\t2. Search for a student's faculty by email\n" +
                  "\t3. Display all University faculties\n" +
                  "\t4. Display all faculties belonging to a field.")
            sub_choice = int(input())
            if sub_choice == 1:
                name = input("Enter Faculty Name: ")
                abbreviation = input("Enter Faculty Abbreviation: ")
                study_field =
