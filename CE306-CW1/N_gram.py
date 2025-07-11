from elasticsearch import Elasticsearch, helpers
import json

# Initialize Elasticsearch
es = Elasticsearch("http://localhost:9200", basic_auth=("elastic", "Febsha123"))

# Load the JSON file
with open(r"C:\ELK\cw1\csvjson (1).json", "r", encoding="utf-8") as file:
    articles = json.load(file)

# Define the new index settings and mappings
index_name = "articles_index_new"
index_mapping = {
    "settings": {
        "analysis": {
            "tokenizer": {
                "ngram_tokenizer": {
                    "type": "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 25,
                    "token_chars": ["letter", "digit"]
                }
            },
            "filter": {
                "stop_filter": {
                    "type": "stop",
                    "stopwords": "_english_"
                },
                "stemmer_filter": {
                    "type": "stemmer",
                    "name": "english"
                }
            },
            "analyzer": {
                "stemmed_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "stop_filter", "stemmer_filter"]
                },
                "ngram_analyzer": {
                    "type": "custom",
                    "tokenizer": "ngram_tokenizer",
                    "filter": ["lowercase"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "case_id": {"type": "integer"},
            "year": {"type": "integer"},
            "r_mth": {"type": "text", "analyzer": "ngram_analyzer"},
            "date": {"type": "date", "format": "MM/dd/yyyy"},
            "intv_nam": {"type": "text", "analyzer": "stemmed_analyzer"},
            "country_residence": {"type": "text", "analyzer": "stemmed_analyzer"},
            "city_residence": {"type": "text", "analyzer": "stemmed_analyzer"},
            "purpose_grp": {"type": "text", "analyzer": "stemmed_analyzer"},
            "purpose": {"type": "text", "analyzer": "stemmed_analyzer"},
            "weights_qtr": {"type": "float"},
            "air_terminal": {"type": "text", "analyzer": "stemmed_analyzer"},
            "sea_terminal": {"type": "text", "analyzer": "stemmed_analyzer"},
            "land_terminal": {"type": "text", "analyzer": "stemmed_analyzer"},
            "main_accomm": {"type": "text", "analyzer": "stemmed_analyzer"},
            "main_hotel": {"type": "text", "analyzer": "stemmed_analyzer"},
            "travel_companion": {
                "type": "nested",
                "properties": {
                    "companion": {"type": "text", "analyzer": "stemmed_analyzer"}
                }
            }
        }
    }
}

# Delete index if it exists and recreate it
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)
es.indices.create(index=index_name, body=index_mapping)

# Prepare bulk index request
actions = []
for doc in articles:
    action = {
        "_index": index_name,
        "_source": {
            "case_id": doc.get("case", 0),
            "year": doc.get("Year", 0),
            "r_mth": doc.get("R.mth", ""),
            "date": doc.get("date", ""),
            "intv_nam": doc.get("intv_nam", ""),
            "country_residence": doc.get("Country_residence", ""),
            "city_residence": doc.get("City_residence", ""),
            "purpose_grp": doc.get("Purpose_grp", ""),
            "purpose": doc.get("Purpose", ""),
            "weights_qtr": doc.get("Weights_QTR", 0.0),
            "air_terminal": doc.get("Air_Terminal", ""),
            "sea_terminal": doc.get("Sea_Terminal", ""),
            "land_terminal": doc.get("Land_Terminal", ""),
            "travel_companion": [
                {"companion": doc.get(f"travel_companion.{i}", "")} for i in range(1, 6) if doc.get(f"travel_companion.{i}")
            ]
        }
    }
    actions.append(action)

# Perform bulk indexing
helpers.bulk(es, actions)
print("Reindexing completed!")

# Analyze text using the ngram_analyzer
analyze_response = es.indices.analyze(
    index=index_name,
    body={
        "analyzer": "ngram_analyzer",
        "text": "Singapore"
    }
)

print("Analyze Response:", analyze_response)
