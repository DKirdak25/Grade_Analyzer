# 📊 Grade Analyzer

![Python](https://img.shields.io/badge/Python-3-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

A powerful Python automation project that analyzes student grades and provides comprehensive statistical insights for educators.

## ✨ Features

- 📈 **Calculate Average Marks** - Compute the mean grade across all students
- 🏆 **Find Highest Mark** - Identify the top score in the class
- 📉 **Find Lowest Mark** - Locate the lowest score
- ✅ **Count Passed Students** - Determine how many students passed (score ≥ 50)
- 🛡️ **Input Validation** - Robust error handling and validation
- 🧪 **Automated Unit Tests** - Comprehensive test coverage
- 🎭 **Mock Testing** - Advanced testing with mocked inputs
- ⚙️ **CI/CD Integration** - GitHub Actions workflow included

## 📂 Project Structure

```
Grade_Analyzer/
│
├── logic.py                 # Core analyzer logic
├── interface.py             # User interface
├── test_analyzer.py         # Unit tests
├── README.md               # Project documentation
└── .github/
    └── workflows/
        └── python-tests.yml # GitHub Actions workflow
```

## 🔧 How It Works

### Business Logic (`logic.py`)

The **Analyzer** class handles all grade analysis:
- Calculates average, highest, and lowest marks
- Counts students who passed (score ≥ 50)
- Validates input data
- Manages student grade collections

### User Interface (`interface.py`)

Handles user interaction:
- Prompts for student grades
- Validates user input
- Displays formatted results
- Manages error recovery

**Architecture Benefits**: Clean separation of concerns makes the code testable, maintainable, and scalable.

## 🚀 Quick Start

### Running the Application

```bash
python interface.py
```

### Example Usage

**Input:**
```
Enter Marks of Student: 30
Enter Marks of Student: 90
Enter Marks of Student: 75
Enter Marks of Student: q
```

**Output:**
```
Average : 65.0
Lowest : 30
Highest : 90
Passed Students : 2
```

## 🧪 Testing

### Run All Tests

```bash
python -m unittest test_analyzer.py
```

Or run all tests in the project:

```bash
python -m unittest
```

### Test Coverage

The test suite validates:
- ✓ Average calculation accuracy
- ✓ Highest/lowest mark identification
- ✓ Passed student counting
- ✓ Invalid data type handling
- ✓ Empty list edge cases
- ✓ User input handling
- ✓ Input recovery mechanisms
- ✓ Mocked keyboard input scenarios

## 🛠️ Technologies & Concepts

### Technologies
- **Python 3** - Core language
- **unittest** - Testing framework
- **unittest.mock** - Input mocking
- **Git & GitHub** - Version control
- **GitHub Actions** - CI/CD automation

### Concepts Practiced
- 🎯 Object-Oriented Programming (OOP)
- ✔️ Input Validation
- 🏗️ Separation of Concerns
- 🧪 Unit Testing
- 🔄 Test Automation
- 🎭 Mocking
- ⚡ Continuous Integration (CI)

## 🔮 Future Enhancements

- [ ] Grade classification (A, B, C, D, F)
- [ ] Student names and ID support
- [ ] File storage and persistence
- [ ] CSV import/export functionality
- [ ] Graphical user interface (GUI)
- [ ] Percentage-based analysis
- [ ] Student performance statistics
- [ ] Batch processing

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built as a learning project to master:
- Python programming fundamentals
- Software testing and automation
- GitHub Actions and CI/CD
- Professional project structure

---

**Contributing**: Contributions, issues, and feature requests are welcome! Feel free to check the [issues](https://github.com/DKirdak25/Grade_Analyzer/issues) page.
