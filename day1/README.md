# Week 4 - Day 1

## Python Backend Setup

### Topics Learned

1. Python Virtual Environment
2. pip
3. Django Installation
4. Django Version Checking
5. Django Project Setup
6. Django App Creation

### Python Version

Python 3.13.15

### Django Version

6.1.1

### What is a Virtual Environment?

A virtual environment creates a separate environment for a Python project. It helps keep project packages separate from other Python projects.

### What is pip?

pip is Python's package installer. It is used to install and manage Python packages.

### What is Django?

Django is a Python web framework used to build web applications and backend APIs.

### Commands Used

```text
python --version
py -m venv venv
venv\Scripts\activate
python -m pip --version
pip install django
django-admin --version
django-admin startproject tasktracker .
python manage.py startapp tasks
python manage.py check
