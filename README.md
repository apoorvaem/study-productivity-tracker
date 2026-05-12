# Study Productivity Tracker

## Overview
The Study Productivity Tracker is a command-line Python application that helps users record, manage, and analyze their study habits. It allows users to track tasks, hours studied, priority levels, and productivity ratings, while providing insights into study productivity.

This project was built to practice file handling, modular programming, input validation, and data analysis in Python.

---

## Features

- Add study session entries (task, hours, priority, productivity)
- View all stored entries
- Search entries by keyword
- Delete entries by keyword
- View productivity summary (total entries and average productivity)
- Input validation

---

## Project Structure

The application is divided into two main components:

- `main.py` (handles user interaction and menu system)
- `tracker.py` (contains all main functionality for data processing and file operations)

Data is stored in `data.txt` and is accessed by both modules.

---

## Example Usage

Each study session entry recorded in the system follows a consistent structure:

```
Task | Hours | Priority | Productivity
```
Below is an example of a set of study session entries:

```
CSC 305 Assignment 1 | 3 hour(s) | medium | 4/5
MATH 202 Midterm 2 Preparation | 1.5 hour(s) | high | 5/5
ANTH 100 Syllabus Review | 0.25 hour(s) | low | 2/5
```


