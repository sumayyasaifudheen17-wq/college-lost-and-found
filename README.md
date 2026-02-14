<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Lost and Found] 🎯

## A simple web-based application designed to help college students report and recover lost items on campus

### Team Name: [Individual]

### Team Members
- Member 1: [Sumayya] - [SSET]

### Hosted Project Link
Not hosted. The application can be run locally by following the setup instructions in this repository.

### Project Description
A web-based lost and found system designed for college campuses that allows users to report lost and found items digitally. The system uses flexible matching to identify possible item matches even when descriptions differ.

### The Problem statement
In college campuses, lost and found items are usually handled informally through notice boards, WhatsApp groups, or word of mouth. This leads to poor visibility, mismatches in item descriptions, and many items never being returned to their rightful owners.

### The Solution
To provide a centralized platform for reporting lost and found items

To improve the chances of matching items using partial description matching

To reduce manual effort and confusion in college lost-and-found processes

---

## Technical Details
The application follows a client–server architecture using a lightweight Python web framework. User inputs from the frontend are processed by the backend, stored in a relational database, and compared using a fuzzy matching algorithm to identify potential matches between lost and found items. The system dynamically updates item listings and removes matched entries once a successful match is detected.


### Technologies/Components Used
Backend

Python – Core programming language used for application logic

Flask – Web framework used to handle routing, request processing, and server-side logic

Frontend

HTML – Structure of the web pages

CSS – Styling and basic user interface design

Database

SQLite – Lightweight relational database used to store lost and found item records

Matching Logic

Python Standard Library – Used to implement fuzzy text matching for comparing item descriptions without requiring exact matches

Development & Version Control

Git – Version control system for tracking code changes

GitHub – Remote repository for project hosting and collaboration
**For Software:**
- Languages used: [Python, HTML, CSS]
- Frameworks used: [Flask (Python web framework)]
- Libraries used: [Flask, SQLite3(Python built-in database module), difflib (Python standard library for fuzzy matching)]
- Tools used: [VS Code, Git, GitHub, Ubuntu Linux]

**For Hardware:**
- Main components: [List main components]
- Specifications: [Technical specifications]
- Tools required: [List tools needed]

---

## Features

- Lost Item Reporting: Users can submit details of items they have lost.

- Found Item Reporting: Users can report items they have found on campus.

- Fuzzy Matching: The system compares item descriptions and identifies possible matches even if descriptions are not identical.

- Automatic Match Handling: When a lost item matches a found item, both entries are removed from the active lists.

---

##Implementation
#For Software:
#Installation
python3 -m venv venv
source venv/bin/activate
pip install flask

#Run
python3 app.py

For Hardware:
Components Required

Not applicable

Circuit Setup

Not applicable

Project Documentation
For Software:
Screenshots (Add at least 3)

![Screenshot1](/home/ubontu/Downloads/Screenshot 2026-02-14 at 06-03-27 College Lost & Found.png)
Home page showing lost and found item submission forms

![Screenshot2](/home/ubontu/Downloads/Screenshot 2026-02-14 at 06-03-39 College Lost & Found.png)
List of reported lost items

![Screenshot3](/home/ubontu/Downloads/Screenshot 2026-02-14 at 06-04-36 College Lost & Found.png)
Matching results between lost and found items

Diagrams

System Architecture:

The frontend built with HTML and CSS collects user input, which is processed by the Flask backend. Data is stored in an SQLite database, and fuzzy matching logic compares item descriptions to find potential matches.

Application Workflow:

Users submit lost or found items, the backend stores the data, performs matching, and updates the displayed lists accordingly.

For Hardware:
Schematic & Circuit

![Circuit](Add your circuit diagram here)
Not applicable

![Schematic](Add your schematic diagram here)
Not applicable

Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
Not applicable

![Build](Add photos of build process here)
Not applicable

![Final](Add photo of final product here)
Not applicable

Additional Documentation
For Web Projects with Backend:
API Documentation

Base URL: http://127.0.0.1:5000

Endpoints

GET /

#Description: Displays the home page with lost and found item forms and lists

#Parameters: None

#Response:

{
  "status": "success",
  "data": "HTML page"
}


POST /add

#Description: Submits a lost or found item to the database

Request Body:

{
  "type": "lost or found",
  "category": "item category",
  "description": "item description"
}


#Response:

{
  "status": "success",
  "message": "Item added successfully"
}

#For Mobile Apps:

#App Flow Diagram

Not applicable

#Installation Guide

Not applicable

##For Hardware Projects:

#Bill of Materials (BOM)

Component | Quantity | Specifications | Price | Link/Source
Not applicable

#Total Estimated Cost: ₹0

#Assembly Instructions

Not applicable

##For Scripts/CLI Tools:

#Command Reference

Not applicable

#Project Demo
Video

Not available

#Additional Demos

Not available

##AI Tools Used (Optional - For Transparency Bonus)

#Tool Used: ChatGPT

Purpose: Code debugging assistance and documentation support

#Key Prompts Used:

"Create a Flask-based lost and found system"

"Implement fuzzy matching for text descriptions"

Percentage of AI-generated code: Approximately 20%

#Human Contributions:

Application design and logic implementation

Database integration

Testing and debugging

##UI structuring

#Team Contributions

Sumayya: Backend development, database design, documentation, testing

#License

This project is licensed under the MIT License - see the LICENSE file for details.
---

Made with ❤️ at TinkerHub
