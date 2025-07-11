import csv
import json
import os

# Corrected file paths
csv_file_path = r"C:\ELK\cw1\cw1_data_tourism.csv"  # Use raw string (r"")
bulk_file_path = r"C:\ELK\cw1\cw1_data_tourism.json"  # Save JSON in the same directory

# Check if the CSV file exists before proceeding
if not os.path.exists(csv_file_path):
    print(f"Error: CSV file '{csv_file_path}' not found. Please check the path.")
else:
    # Convert CSV to bulk JSON format
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(bulk_file_path, mode='w', encoding='utf-8') as bulk_file:
            for row in csv_reader:
                # Metadata line for bulk API
                index_metadata = {
                    "index": {
                        "_index": "data_tourism_index"
                    }
                }

                bulk_file.write(json.dumps(index_metadata) + '\n')
                bulk_file.write(json.dumps(row) + '\n')

    print(f"CSV file has been successfully converted to bulk format in {bulk_file_path}")
