# Hangman Game - Test-Driven Development Implementation

A comprehensive implementation of the classic Hangman word-guessing game, developed using **Test-Driven Development (TDD)** methodology for the PRT582 Software Unit Testing course.

##  Game Features

- **Two Difficulty Levels**: Basic (single words) and Intermediate (phrases)
- **Timer-Based Gameplay**: 15-second countdown for each guess
- **Life Management System**: 6 lives per game with strategic gameplay
- **Input Validation**: Comprehensive validation for user inputs
- **ASCII Art Display**: Visual hangman representation
- **Clean Console Interface**: User-friendly menu and game state display

##  Test-Driven Development

This project demonstrates rigorous TDD methodology:

- **Red-Green-Refactor Cycle**: Every feature developed following TDD principles
- **Comprehensive Test Coverage**: Extensive test suite covering all functionality
- **Automated Testing**: pytest framework with coverage analysis
- **Code Quality Assurance**: flake8 and pylint integration

##  Project Metrics

- **Code Quality**: 9.66/10 pylint rating
- **Style Compliance**: 100% flake8 compliant
- **Test Success Rate**: 100% passing tests
- **Documentation**: Complete inline documentation

##  Prerequisites

Before running this project, ensure you have:

- **Python 3.7 or higher** installed on your system
- **pip** package manager (comes with Python)
- **Git** (for cloning the repository)
- **Command line access** (Command Prompt on Windows, Terminal on Mac/Linux)

### Check Your Python Version
```bash
python --version
# Should show: Python 3.7.x or higher
```

### Check pip Installation
```bash
pip --version
# Should show pip version information
```

##  Installation & Setup

### Step 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/anandjaiswal10101/hangman-tdd-project.git

# Navigate to project directory
cd hangman-tdd-project
```

### Step 2: Create Virtual Environment

**Windows:**
```cmd
# Create virtual environment
python -m venv hangman_env

# Activate virtual environment
hangman_env\Scripts\activate

# You should see (hangman_env) at the beginning of your prompt
```

**Mac/Linux:**
```bash
# Create virtual environment
python -m venv hangman_env

# Activate virtual environment
source hangman_env/bin/activate

# You should see (hangman_env) at the beginning of your prompt
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
pip list
```

**Expected packages:**
- pytest==7.4.3
- pytest-cov==4.1.0
- flake8==6.1.0
- pylint==3.0.3

##  Running the Game

### Start the Hangman Game
```bash
# Make sure virtual environment is activated
# You should see (hangman_env) in your prompt

python hangman_game.py
```

### Game Controls
1. **Choose difficulty level** (1 for Basic, 2 for Intermediate, 3 to Quit)
2. **Enter single letters** when prompted
3. **You have 15 seconds** per guess
4. **Type 'quit'** during gameplay to exit
5. **Follow on-screen instructions**

##  Running Tests

### Run All Tests
```bash
# Basic test run
pytest test_hangman_game.py

# Verbose output (recommended)
pytest test_hangman_game.py -v

# Very detailed output
pytest test_hangman_game.py -vv
```

### Run Tests with Coverage Analysis
```bash
# Generate coverage report
pytest --cov=hangman_game --cov-report=html test_hangman_game.py

# View coverage in terminal
pytest --cov=hangman_game --cov-report=term test_hangman_game.py

# Open HTML coverage report (Windows)
start htmlcov\index.html

# Open HTML coverage report (Mac)
open htmlcov/index.html

# Open HTML coverage report (Linux)
xdg-open htmlcov/index.html
```

##  Code Quality Checks

### Check Code Style (flake8)
```bash
# Check both main files
flake8 hangman_game.py test_hangman_game.py

# No output means no style violations (perfect!)
```

### Check Code Quality (pylint)
```bash
# Analyze main game file
pylint hangman_game.py

# Expected output: "Your code has been rated at 9.66/10"
```

### Check All Quality Metrics at Once
```bash
# Run all quality checks
pytest test_hangman_game.py -v && flake8 hangman_game.py test_hangman_game.py && pylint hangman_game.py
```

##  Project Structure

```
hangman-tdd-project/
├── hangman_game.py          # Main game implementation
├── test_hangman_game.py     # Comprehensive test suite
├── requirements.txt         # Project dependencies
├── README.md               # This file
├── .gitignore             # Git ignore patterns
└── htmlcov/              # Coverage reports (generated after testing)
```

##  Game Rules

### Objective
Guess the hidden word or phrase before running out of lives!

### How to Play

1. **Choose Your Level**:
   - **Basic (1)**: Single words like "PYTHON", "COMPUTER"
   - **Intermediate (2)**: Phrases like "TEST DRIVEN DEVELOPMENT"

2. **Make Your Guesses**:
   - Enter **one letter at a time**
   - You have **15 seconds** per guess
   - Timer starts when you see "Enter a letter:"

3. **Manage Your Lives**:
   - Start with **6 lives**
   - Lose a life for **incorrect guesses**
   - Lose a life if **time runs out**

4. **Win or Lose**:
   - **Win**: Guess all letters before running out of lives
   - **Lose**: Lives reach zero

### Example Gameplay
```
==================================================
           WELCOME TO HANGMAN GAME
==================================================
1. Basic Level (Words)
2. Intermediate Level (Phrases)
3. Quit Game
==================================================
Enter your choice (1-3): 1

Starting Basic Level!
Try to guess the word/phrase. You have 6 lives.

----------------------------------------
Level: Basic
Lives: 6/6
Word/Phrase: _ _ _ _ _ _
----------------------------------------

You have 15 seconds to make a guess!
Enter a letter: p
Good guess! 'P' is in the answer.
```

##  Test Categories

The test suite includes:

- **Initialization Tests**: Game setup and configuration
- **Display Tests**: Word/phrase rendering logic
- **Validation Tests**: Input validation and error handling
- **Game Logic Tests**: Core gameplay mechanics
- **Timer Tests**: Countdown and threading functionality
- **State Management Tests**: Game state tracking
- **Integration Tests**: End-to-end game scenarios

##  Development Workflow

This project was developed using TDD methodology:

1. **Red Phase**: Write failing tests first
2. **Green Phase**: Write minimal code to pass tests
3. **Refactor Phase**: Improve code while keeping tests green

### Running Development Checks
```bash
# Full development workflow check
pytest test_hangman_game.py -v
pytest --cov=hangman_game --cov-report=term test_hangman_game.py
flake8 hangman_game.py test_hangman_game.py
pylint hangman_game.py
```

## 🎓 Educational Objectives

This project demonstrates:

- **TDD Methodology**: Practical application of test-first development
- **Python Best Practices**: Professional coding standards
- **Software Testing**: Comprehensive test strategy implementation
- **Code Quality**: Static analysis and continuous improvement
- **Documentation**: Clear, maintainable code documentation

## 📄 License

This project is created for educational purposes as part of the PRT582 Software Unit Testing course.

##  Author

**Student**:ANAND JAISWAL  
**Course**: PRT582 Software Unit Testing  
**Institution**: [Your Institution]  
**Date**: [Current Date]

## 🙏 Acknowledgments

- Course instructor for TDD methodology guidance
- pytest community for excellent testing framework
- Python community for comprehensive development tools

---

*This project showcases professional software development practices through Test-Driven Development methodology, demonstrating the importance of testing in creating robust, maintainable software.*