# PostgreSQL Student Management Application

This Python application allows users to perform basic CRUD operations on a PostgreSQL database of student records using a command-line interface.

## Features

- Retrieve and display all student records.
- Add a new student record.
- Update a student's email address.
- Delete a student record.

## Requirements

- Python 3.x
- psycopg2 library

## Getting Started

1. Once you've cloned the repository, navigate to the project directory:
   ```bash
   cd 3005a3
   ```
2. Install `psycopg2`.
   ```bash
   pip install psycopg2
   ```
3. Set up your PostgreSQL database and create the `students` table using the provided schema in `schema.sql`.
4. Open `main.py` and replace the placeholder values with your actual connection details for the database.
5. Run the application
   ```bash
   python main.py
   ```

## Video Link

https://youtu.be/9kukSINc94Q