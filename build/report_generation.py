import pandas as pd
import os

def generate_html_report(df, file_path):
    html_content = df.to_html()
    with open(file_path, "w") as f:
        f.write(f"<html><body><h1>Data Analysis Report</h1>{html_content}</body></html>")

def main():
    processed_data_path = os.path.join("data", "processed", "processed_data.csv")
    report_path = os.path.join("reports", "report.html")
    
    data = pd.read_csv(processed_data_path)
    generate_html_report(data.describe(), report_path)

if __name__ == "__main__":
    main()
