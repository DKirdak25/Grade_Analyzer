Student Grade Analyzer

A simple Python project that analyzes student marks and demonstrates software engineering fundamentals such as testing, mocking, input validation, and project structure.

Features

- Calculate average marks
- Find highest mark
- Find lowest mark
- Count passed students
- Input validation
- Automated unit tests
- Mocked user input testing

Project Structure

Automation_Project/
│
├── logic.py
├── interface.py
├── test_analyzer.py
├── README.md
└── .github/
    └── workflows/
        └── python-tests.yml

How It Works

The project is separated into two parts:

Business Logic ("logic.py")

Contains the "Analyzer" class responsible for:

- Calculating average marks
- Finding highest mark
- Finding lowest mark
- Counting passed students
- Validating constructor input

User Interface ("interface.py")

Handles:

- User input
- Input validation
- Displaying analysis results

This separation makes the code easier to test and maintain.

Example

Input:

Enter Marks of Student: 30
Enter Marks of Student: 90
Enter Marks of Student: q

Output:

Average : 60.0
Lowest : 30
Highest : 90
Passed Students : 1

Running the Application

python interface.py

Running Tests

python -m unittest test_analyzer.py

or

python -m unittest

Test Coverage

The test suite verifies:

- Average calculation
- Highest mark calculation
- Lowest mark calculation
- Passed student count
- Invalid data types
- Empty mark lists
- User input handling
- Invalid input recovery
- Mocked keyboard input

Technologies Used

- Python 3
- unittest
- unittest.mock
- Git
- GitHub
- GitHub Actions

Concepts Practiced

- Object-Oriented Programming (OOP)
- Input Validation
- Separation of Concerns
- Unit Testing
- Test Automation
- Mocking
- Continuous Integration (CI)

Future Improvements

- Grade classification (A, B, C, D, F)
- Student names support
- File storage
- CSV import/export
- Graphical user interface
- Percentage analysis

Author

Built as a learning project to practice Python programming, testing, automation, and GitHub Actions.
