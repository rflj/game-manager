#!/bin/bash
set -e

# Load virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

python ./manager/manage.py runserver
