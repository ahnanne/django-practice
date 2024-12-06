# django-practice
A demo project to practice Django.

# Installation
**1. Clone this repository.**

**2. Set up a virtual environment.**

```bash
python -m venv env
```

**3. Activate venv.**

Linux/macOS
```bash
source env/bin/activate
```
Windows (Command Prompt)
```bash
. env/Scripts/activate
```
Windows (PowerShell)
```bash
. env/Scripts/Activate.ps1
```

**4. Install dependencies.**

For production dependencies only:
```bash
pip install -r requirements.txt
```
For both production and development dependencies:
```bash
pip install -r requirements.txt -r requirements-dev.txt
```

**5. Run the development server.**

```bash
python manage.py runserver
```
Then navigate to `http://127.0.0.1:8000`.