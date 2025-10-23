# Student Grade Management System

A Python-based Student Grade Management System that allows educators to manage student records, calculate grades, and generate academic reports efficiently.

## Features

### 📦 Core Functionality
- **Student Management**: Create and manage student records with unique IDs and names
- **Grade Management**: Add multiple numeric grades (0-100 range) to student profiles
- **Grade Calculations**: Automatically calculate average grades and convert to letter grades
- **Academic Status**: Determine pass/fail status based on performance
- **Input Validation**: Robust error handling for invalid inputs

### 🌟 Advanced Features
- **Honor Roll Detection**: Identify high-achieving students (average ≥ 90)
- **Grade Removal**: Delete grades by index with bounds checking
- **Comprehensive Reporting**: Generate detailed student summary reports

## Grade Scale
- **A**: 90–100
- **B**: 80–89  
- **C**: 70–79
- **D**: 60–69
- **F**: <60

## Academic Standards
- **Passing Grade**: Average of 60 or higher
- **Honor Roll**: Average of 90 or higher

## Usage

### Basic Operations
```python
# Create a student
student = Student("123", "John Doe")

# Add grades
student.add_grades(100)
student.add_grades(95)
student.add_grades(85)

# Generate report
student.report()
```

### Sample Output
```
ID: 123
Name is: John Doe
Grades Count: 3
Average: 93.33
Letter Grade: A
Status: Passed
Honor Roll: Yes
```

## Error Handling
The system includes comprehensive validation for:
- Grade values (must be numbers between 0-100)
- Grade indices (must be within valid range)
- Student information (non-empty names and IDs)

## Class Methods

### Student Class
- `__init__(student_id, name)`: Initialize student record
- `add_grades(grade)`: Add a validated grade
- `calc_average()`: Calculate grade average
- `calculate_letter_grade()`: Determine letter grade
- `check_pass_fail()`: Set pass/fail status
- `check_honor()`: Check honor roll eligibility
- `delete_grade(index)`: Remove grade by index
- `report()`: Generate comprehensive student report

## Requirements
- Python 3.x
- No external dependencies

## Getting Started
Run the included test file to see the system in action:
```bash
python test.py
```