import requests
import csv
import json

API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMxMTU0NDYzMiwiYWFpIjoxMSwidWlkIjo1NDU4Njg3MCwiaWFkIjoiMjAyNC0wMS0xOFQwNDoxNjoyMi4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MjA4MTU4NjcsInJnbiI6ImFwc2UyIn0.ixUeIGRE7OgBQwBfssTmP_8T-agBAA4XZ2sDwTHCA5o'
API_URL = 'https://api.monday.com/v2/boards/1838668631'
CSV_FILE_PATH = 'contacts_sample_import-1.csv'

def import_data_to_monday(data):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY,
    }
    
    item = str(data)
    payload = {
            "query": "mutation {create_item (board_id: 1838668631, group_id: \"samples\", item_name: \"new item\") {id}}" 
        }
    # print(payload)
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        print("Data imported successfully.")
    else:
        print(f"Failed to import data. Status code: {response.status_code}")
        # print(response.text)

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data_list = [row for row in reader]

    return data_list

def main():
    data_list = read_csv(CSV_FILE_PATH)
    for i in data_list[:1]:
        import_data_to_monday(i)

if __name__ == "__main__":
    main()
