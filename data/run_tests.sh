#!/bin/bash

# Activate virtual environment (Windows path)
source ../venv/Scripts/activate

# Run pytest
pytest

# Check exit code and return accordingly
if [ $? -eq 0 ]; then
    echo "All tests passed."
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
