from elasticsearch import Elasticsearch, helpers
import json

# Initialize Elasticsearch
es = Elasticsearch("http://localhost:9200", basic_auth=("elastic", "Febsha123"))

# Load the JSON file
with open(r"C:\ELK\cw1\csvjson (1).json", "r", encoding="utf-8") as file:
    articles = json.load(file)

# Prepare bulk index request
actions = []
for doc in articles:
    action = {
        "_index": "articles_index",
        "_source": {
            "case_id": doc["case"],
            "year": doc["Year"],
            "purpose": doc["Purpose"],
            "accommodation": doc["MainAccomm"],
            "travel_type": doc["travel_type"],
            "interviewer": doc["intv_nam"],
            "country_residence": doc["Country_residence"],
            "city_residence": doc["City_residence"]
        }
    }
    actions.append(action)

# Perform bulk indexing
helpers.bulk(es, actions)

print("Indexing completed!")
