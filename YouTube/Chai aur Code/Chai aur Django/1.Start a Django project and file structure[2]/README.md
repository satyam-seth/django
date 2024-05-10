[YouTube Video Link](https://youtu.be/CLDDcXV4H50?si=VB3MWNjvNT8jaReX)

1. Install [uv](https://pypi.org/project/uv/) package

   ```bash
   pip install uv
   ```

2. Create virtual environment using uv

   ```
   uv venv
   ```

3. Activate virtual environment

   - On macOS and Linux.

     ```bash
     source .venv/bin/activate
     ```

   - On Windows.

     ```bash
     .venv\Scripts\activate
     ```

4. Install [Django](https://pypi.org/project/Django/) package

   ```bash
   uv pip install Django
   ```

5. Create Django project

   ```bash
   django-admin startproject chaiaurDjango
   ```

6. Go to inner project directory

   ```bash
   cd chaiaurDjango
   ```

7. Run server

   ```bash
   python manage.py runserver
   ```

8. Deactivate virtual environment

   ```bash
   deactivate
   ```
