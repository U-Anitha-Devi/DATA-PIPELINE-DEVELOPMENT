import pandas as pd
def extract_data(file_path):
    print("🔹 Extracting data...")
    df = pd.read_csv(file_path)
    print("\nOriginal Data:\n", df)
    return df
def transform_data(df):
    print("🔹 Transforming data...")
    df_clean = df.dropna()
    df_clean.columns = [col.lower() for col in df_clean.columns]
    print("\nCleaned Data:\n", df_clean)
    return df_clean
def load_data(df, output_path):
    print("🔹 Loading data...")
    df.to_csv(output_path, index=False)
    print(f"\n✅ Data successfully saved to {output_path}")
def run_pipeline():
    input_file = 'sample_data.csv'      
    output_file = 'cleaned_data.csv'    
    data = extract_data(input_file)
    clean_data = transform_data(data)
    load_data(clean_data, output_file)

if __name__ == "__main__":
    run_pipeline()
