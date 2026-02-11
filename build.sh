#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
```

### 3. `.gitignore`
```
# Python
*.py[cod]
*$py.class
*.so
__pycache__/
*.pyc
.Python

# Django
*.log
db.sqlite3
db.sqlite3-journal
/media
/staticfiles

# Environment
.env
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Local database credentials
local_settings.py