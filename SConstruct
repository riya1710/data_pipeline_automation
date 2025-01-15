import os
from SCons.Script import Command

# Define absolute paths based on your project structure
raw_data = r"C:\Users\Riya Malhotra\Desktop\data_pipeline\data\raw\data.csv"
processed_data = r"C:\Users\Riya Malhotra\Desktop\data_pipeline\data\processed\processed_data.csv"
report = r"C:\Users\Riya Malhotra\Desktop\data_pipeline\reports\report.html"

# Define the absolute path to the src directory
src_dir = r"C:\Users\Riya Malhotra\Desktop\data_pipeline\src"

# Define the full path to python.exe
python_path = r"C:\Users\Riya Malhotra\AppData\Local\Programs\Python\Python311\python.exe"  # Adjust this path

# Step 1: Data Processing
Command(
    target=processed_data,
    source=raw_data,
    action=f"\"{python_path}\" \"{os.path.join(src_dir, 'data_processing.py')}\""
)

# Step 2: Report Generation
Command(
    target=report,
    source=processed_data,
    action=f"\"{python_path}\" \"{os.path.join(src_dir, 'report_generation.py')}\""
)
