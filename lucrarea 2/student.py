from datetime import date

class Student:
    def __init__(self, first_name, last_name, email, enrollment_date, date_of_birth, faculty, is_graduated):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth
        self.faculty = faculty
        self.is_graduated = is_graduated

    def __str__(self):
        return f"Student Name: {self.first_name} {self.last_name}\n" \
               f"Student Email: {self.email}\n" \
               f"Enrollment Date: {self.enrollment_date}\n" \
               f"Date of Birth: {self.date_of_birth}\n" \
               f"Faculty: {self.faculty}\n" \
               f"Is Graduated: {self.is_graduated}"

    def set_graduated(self, graduated):
        self.is_graduated = graduated

    def get_faculty(self):
        return self.faculty

    def set_faculty(self, faculty):
        self.faculty = faculty

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_enrollment_date(self):
        return self.enrollment_date

    def set_enrollment_date(self, enrollment_date):
        self.enrollment_date = enrollment_date

    def get_date_of_birth(self):
        return self.date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth


# Example usage:
enrollment_date = date(2022, 1, 1)
date_of_birth = date(2000, 1, 1)
faculty_example = "ExampleFaculty"

student_example = Student("John", "Doe", "john.doe@example.com", enrollment_date, date_of_birth, faculty_example, False)

print(str(student_example))
