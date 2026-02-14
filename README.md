# College Lost and Found System

A simple web-based application designed to help college students report and recover lost items on campus.

## Problem Statement
Students frequently lose personal belongings on college campuses, and there is no centralized platform to report or retrieve lost and found items efficiently.

## Solution
This project provides a lightweight Lost and Found portal where users can:
- Report items as Lost or Found
- View all reported items
- See possible matches using fuzzy matching
- Resolve matched items once recovered

The system accounts for human variation in descriptions instead of relying on exact text matches.

## Features
- Separate Lost and Found listings
- Fuzzy matching for similar item names
- Highlighted matching keywords in descriptions
- Option to mark items as resolved
- SQLite database for storage

## Tech Stack
- Python 3
- Flask
- SQLite
- HTML (Jinja templates)

## How to Run the Project

1. Clone the repository
2. Navigate to the project directory
3. Create and activate a virtual environment
4. Install dependencies
5. Run the Flask application

Example commands:
python3 -m venv venv
source venv/bin/activate
pip install flask
python3 app.py



Then open:
http://127.0.0.1:5000/

## Future Improvements
- User authentication
- Confidence score for matches
- Search and filter options
- Improved UI styling

## Author
Built as a hackathon project.
