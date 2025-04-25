import os
from flask import Flask

app = Flask(__name__)

# Ensure uploads folder exists
os.makedirs('uploads', exist_ok=True)

# Clean out contents of uploads folder
for filename in os.listdir('uploads'):
  file_path = os.path.join('uploads', filename)
  try:
    if os.path.isfile(file_path):
      os.remove(file_path)
  except Exception as e:
    print(f"Error removing {file_path}: {e}")

from app import routes