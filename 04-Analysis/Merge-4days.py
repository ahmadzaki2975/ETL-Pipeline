import pandas as pd
import os

# Daftar nama file yang akan digabungkan
file_names = [
    'mergedData_2023-11-20.csv',
    'mergedData_2023-11-21.csv',
    'mergedData_2023-11-22.csv',
    'mergedData_2023-11-23.csv',
    'mergedData_2023-11-24.csv',
    'mergedData_2023-11-26.csv',
    'mergedData_2023-11-27.csv',
    'mergedData_2023-11-28.csv'
]

# Membuat list untuk menyimpan DataFrames dari setiap file CSV
dataframes = []

# Membaca setiap file dan menyimpannya dalam list
for file_name in file_names:
    file_path = os.path.join('/Users/erikuncoro/Documents/Project_Rekdat/ETL-Pipeline/04-Analysis/merge_csv/', file_name)
    df = pd.read_csv(file_path)
    dataframes.append(df)

# Menggabungkan semua DataFrames menjadi satu DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Menyimpan DataFrame yang telah digabungkan ke dalam file CSV
output_file_path = '/Users/erikuncoro/Documents/Project_Rekdat/ETL-Pipeline/04-Analysis/merge_csv/8-days-merge.csv'
merged_df.to_csv(output_file_path, index=False)
print(f"Data telah digabungkan dan disimpan dalam: {output_file_path}")
