import csv
import json
import os

# file paths
csv_file_path = r"C:\ELK\cw1\cw1_data_tourism.csv"
bulk_file_path = r"C:\ELK\cw1\cw1_data_tourism.json"  # Save JSON in the same directory

# Check if the CSV file exists before proceeding
if not os.path.exists(csv_file_path):
    print(f"Error: CSV file '{csv_file_path}' not found. Please check the path.")
else:
    # Convert CSV to bulk JSON format
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:  # Using utf-8-sig to remove BOM
        csv_reader = csv.DictReader(csv_file)

        # Open the bulk file in write mode
        with open(bulk_file_path, mode='w', encoding='utf-8', newline='\n') as bulk_file: #added newline='\n'
            for index, row in enumerate(csv_reader, start=1):
                # Prepare the bulk request's metadata for indexing
                index_metadata = {
                    "index": {
                        "_index": "tourism"
                    }
                }

                # Write the index metadata and the data row to the bulk file
                try:
                    # Write metadata first
                    bulk_file.write(json.dumps(index_metadata) + '\n')
                    # Write actual data as the next line
                    bulk_file.write(json.dumps(row) + '\n')

                except Exception as e:
                    print(f"Error processing row {index}: {e}")

            # Ensure that the file ends with a newline (important to make the bulk request valid)
            bulk_file.write('\n')  # Add final newline after the last entry to terminate properly

    print(f"CSV file has been successfully converted to bulk format in {bulk_file_path}")