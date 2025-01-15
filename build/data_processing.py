import pandas as pd
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    # Example preprocessing: drop missing values, filter rows, etc.
    df = df.dropna()
    return df

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def main():
    raw_data_path = os.path.join("data", "raw", "data.csv")
    processed_data_path = os.path.join("data", "processed", "processed_data.csv")
    
    data = load_data(raw_data_path)
    cleaned_data = clean_data(data)
    save_data(cleaned_data, processed_data_path)

if __name__ == "__main__":
    main()
