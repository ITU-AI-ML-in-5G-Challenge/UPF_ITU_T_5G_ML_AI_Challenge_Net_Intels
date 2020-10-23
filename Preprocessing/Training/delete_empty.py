# This code is to remove empty rows in a given CSV
import pandas as pd

def delete_empty_rows(file_path, new_file_path):
    data = pd.read_csv(file_path, skip_blank_lines=True)
    data.dropna(how="all", inplace=True)
    data.to_csv(new_file_path, header=True)

delete_empty_rows('Combined_rssi_corrected_proper_sinr.csv', 'Combined_rssi_corrected_proper_sinr_row_fixed.csv')
