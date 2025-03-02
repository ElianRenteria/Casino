#!/bin/bash

# Navigate to project directory
cd "$(dirname "$0")"

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Install required dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Run the main Python script
python main.py

# Deactivate virtual environment
deactivate

