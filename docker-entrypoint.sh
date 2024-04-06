#!/bin/bash

# Run Django tests
python manage.py test

# Check the exit code of the test command
if [ $? -eq 0 ]; then
  # If tests pass, start the server
  python manage.py runserver 0.0.0.0:8000
else
  # If tests fail, exit with a non-zero status code
  echo "Tests failed. Exiting..."
  exit 1
fi