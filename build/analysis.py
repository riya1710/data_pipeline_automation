import pandas as pd
import os

def analyze_data(df):
    summary = df.describe()
    return summary

def main():
    processed_data_path = os.path.join("data", "processed", "processed_data.csv")
    
    data = pd.read_csv(processed_data_path)
    analysis_result = analyze_data(data)
    
    print(analysis_result)

if __name__ == "__main__":
    main()
