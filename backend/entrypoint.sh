#!/bin/bash

# Abort on any error (including if wait-for-it fails).
set -e

# Wait for the backend to be up, if we know where it is.
if [ -n "$MYSQL_HOST" ]; then
  ./wait-for-it.sh $MYSQL_HOST:3306 -t 30
fi
if [ -n "$NEO4J_HOST" ]; then
  ./wait-for-it.sh $NEO4J_HOST:7687 -t 60
fi

# Run the main container command.
cd src/server
alembic upgrade head
python main.py