import sys
import os

print(f"Python executable: {sys.executable}")
print(f"Virtual env: {os.environ.get('VIRTUAL_ENV', 'Not in a virtual environment')}")
