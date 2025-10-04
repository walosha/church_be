#!/bin/bash

# Exit on error
set -e

# Wait for database to be ready (if using PostgreSQL/MySQL)
echo "Waiting for database..."
sleep 5

# Run migrations
echo "Running migrations..."
python /code/church/manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python /code/church/manage.py collectstatic --noinput

# Start the application
echo "Starting application..."
exec "$@"