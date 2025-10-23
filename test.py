"""Student Grade Management System"""


class Student:
    """Represents a student with grades and academic status"""

    def __init__(self, student_id, name):
        """Initialize a student with ID and name"""
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter = "F"

    def add_grades(self, grade):
        """Add a grade to the student's record"""
        if not isinstance(grade, (int, float)):
            raise ValueError("Grade must be a number")
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        self.grades.append(grade)

    def calc_average(self):
        """Calculate the average of all grades"""
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total += grade
        average = total / len(self.grades)
        return average

    def calculate_letter_grade(self):
        """Calculate letter grade based on average"""
        avg = self.calc_average()
        if avg >= 90:
            self.letter = "A"
        elif avg >= 80:
            self.letter = "B"
        elif avg >= 70:
            self.letter = "C"
        elif avg >= 60:
            self.letter = "D"
        else:
            self.letter = "F"
        return self.letter

    def check_pass_fail(self):
        """Determine if student passed or failed"""
        if self.calc_average() >= 60:
            self.is_passed = "Passed"
        else:
            self.is_passed = "Failed"
        return self.is_passed

    def check_honor(self):
        """Check if student qualifies for honor roll"""
        if self.calc_average() >= 90:
            self.honor = "Yes"
        else:
            self.honor = "No"
        return self.honor

    def delete_grade(self, index):
        """Delete a grade by index"""
        if index < 0 or index >= len(self.grades):
            raise IndexError("Grade index out of range")
        del self.grades[index]

    def report(self):
        """Generate a formatted report of student information"""
        self.calculate_letter_grade()
        self.check_pass_fail()
        self.check_honor()
        print("ID: " + self.student_id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print("Average: " + str(self.calc_average()))
        print("Letter Grade: " + self.letter)
        print("Status: " + self.is_passed)
        print("Honor Roll: " + self.honor)


def start_run():
    """Main function to test the Student class"""
    student = Student("123", "John Doe")
    student.add_grades(100)
    student.add_grades(95)
    student.add_grades(85)
    student.calc_average()
    student.check_honor()
    student.report()


start_run()
