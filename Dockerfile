FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update

# Make working directory
RUN mkdir /opt/ref-manager
WORKDIR /opt/ref-manager

# Copy files
COPY requirements.txt .
COPY /manager .
COPY /scripts .

# Install dependencies
RUN pip install -r requirements.txt

# Expose 80 for app
EXPOSE 80

# Run django develop
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]