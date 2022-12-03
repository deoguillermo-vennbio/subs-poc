#!/bin/sh
echo "Container started at $(date)"
echo "Starting uvicorn..."
uvicorn app.main:app --host $HOST --port $PORT --reload
