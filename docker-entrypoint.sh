#!/bin/bash

# Run Django tests 
python library/manage.py makemigrations 
python library/manage.py migrate 
python library/manage.py test

# Check the exit code of the test command
if [ $? -eq 0 ]; then
  # If tests pass, start the server
  python library/manage.py runserver 0.0.0.0:8000
else
  # If tests fail, exit with a non-zero status code
  echo "Tests failed. Exiting..."
  exit 1
fi