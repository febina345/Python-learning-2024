from elasticsearch import Elasticsearch, helpers
import json

# Initialize Elasticsearch
es = Elasticsearch("http://localhost:9200", basic_auth=("elastic", "Febsha123"))

# Load the JSON file
with open(r"C:\ELK\cw1\csvjson (1).json", "r", encoding="utf-8") as file:
    articles = json.load(file)

# Define the index with settings for keyword selection, n-gram extraction, stopword removal, stemming, and tf-idf
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
                "custom_analyzer": {
                    "type": "custom",
                    "tokenizer": "ngram_tokenizer",
                    "filter": ["lowercase", "stop_filter", "stemmer_filter"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "case_id": {"type": "integer"},
            "year": {"type": "integer"},
            "r_mth": {"type": "text", "analyzer": "custom_analyzer"},
            "date": {"type": "date", "format": "MM/dd/yyyy"},
            "intv_nam": {"type": "text", "analyzer": "custom_analyzer"},
            "country_residence": {"type": "text", "analyzer": "custom_analyzer"},
            "city_residence": {"type": "text", "analyzer": "custom_analyzer"},
            "purpose_grp": {"type": "text", "analyzer": "custom_analyzer"},
            "purpose": {"type": "text", "analyzer": "custom_analyzer"},
            "weights_qtr": {"type": "float"},
            "air_terminal": {"type": "text", "analyzer": "custom_analyzer"},
            "sea_terminal": {"type": "text", "analyzer": "custom_analyzer"},
            "land_terminal": {"type": "text", "analyzer": "custom_analyzer"},
            "langint": {"type": "text", "analyzer": "custom_analyzer"},
            "first_visit": {"type": "text", "analyzer": "custom_analyzer"},
            "length_stay": {"type": "text", "analyzer": "custom_analyzer"},
            "travel_type": {"type": "text", "analyzer": "custom_analyzer"},
            "gender": {"type": "text", "analyzer": "custom_analyzer"},
            "occupation": {"type": "text", "analyzer": "custom_analyzer"},
            "industry": {"type": "text", "analyzer": "custom_analyzer"},
            "designation": {"type": "text", "analyzer": "custom_analyzer"},
            "designation_oth": {"type": "text", "analyzer": "custom_analyzer"},
            "shop_fash": {"type": "float"},
            "shop_jew": {"type": "float"},
            "shop_wat": {"type": "float"},
            "shop_well": {"type": "float"},
            "shop_food": {"type": "float"},
            "shop_gift": {"type": "float"},
            "shop_ctec": {"type": "float"},
            "shop_anti": {"type": "float"},
            "shop_oth": {"type": "float"},
            "shop_any": {"type": "float"},
            "totacc": {"type": "float"},
            "totfnb": {"type": "float"},
            "tottran": {"type": "float"},
            "totbiz": {"type": "float"},
            "totedu": {"type": "float"},
            "totmedi": {"type": "float"},
            "tototh": {"type": "float"},
            "totshopping": {"type": "float"},
            "totexp": {"type": "float"},
            "main_accomm": {"type": "text", "analyzer": "custom_analyzer"},
            "main_hotel": {"type": "text", "analyzer": "custom_analyzer"},
            "travel_companion": {
                "type": "nested",
                "properties": {
                    "companion": {"type": "text", "analyzer": "custom_analyzer"}
                }
            }
        }
    }
}

# Create the index with mappings
es.indices.create(index="articles_index3", body=index_mapping, ignore=400)

# Prepare bulk index request
actions = []
for doc in articles:
    action = {
        "_index": "articles_index4",
        "_source": {
            "case_id": doc["case"],
            "year": doc["Year"],
            "r_mth": doc["R.mth"],
            "date": doc["date"],
            "intv_nam": doc["intv_nam"],
            "country_residence": doc["Country_residence"],
            "city_residence": doc["City_residence"],
            "purpose_grp": doc["Purpose_grp"],
            "purpose": doc["Purpose"],
            "weights_qtr": doc["Weights_QTR"],
            "air_terminal": doc["Air_Terminal"],
            "sea_terminal": doc["Sea_Terminal"],
            "land_terminal": doc["Land_Terminal"],
            "langint": doc["langint"],
            "first_visit": doc["1st_visit"],
            "length_stay": doc["length_stay"],
            "travel_type": doc["travel_type"],
            "gender": doc["f1_gender"],
            "occupation": doc["f3_occupation"],
            "industry": doc["f4_industry"],
            "designation": doc["f5_designation"],
            "designation_oth": doc.get("f5_designation.oth", ""),
            "shop_fash": doc["shop_$fash"],
            "shop_jew": doc["shop_$jew"],
            "shop_wat": doc["shop_$wat"],
            "shop_well": doc["shop_$well"],
            "shop_food": doc["shop_$food"],
            "shop_gift": doc["shop_$gift"],
            "shop_ctec": doc["shop_$ctec"],
            "shop_anti": doc["shop_$anti"],
            "shop_oth": doc["shop_$oth"],
            "shop_any": doc["shop_$any"],
            "totacc": doc["totacc_$"],
            "totfnb": doc["totfnb_$"],
            "tottran": doc["tottran_$"],
            "totbiz": doc["totbiz_$"],
            "totedu": doc["totedu_$"],
            "totmedi": doc["totmedi_$"],
            "tototh": doc["tototh_$"],
            "totshopping": doc["totshopping_$"],
            "totexp": doc["totexp_$"],
            "main_accomm": doc["MainAccomm"],
            "main_hotel": doc["MainHotel"],
            "travel_companion": [
    {"companion": doc.get("travel_companion.1")} if doc.get("travel_companion.1") else None,
    {"companion": doc.get("travel_companion.2")} if doc.get("travel_companion.2") else None,
    {"companion": doc.get("travel_companion.3")} if doc.get("travel_companion.3") else None,
    {"companion": doc.get("travel_companion.4")} if doc.get("travel_companion.4") else None,
    {"companion": doc.get("travel_companion.5")} if doc.get("travel_companion.5") else None
]

        }
    }
    actions.append(action)

# Perform bulk indexing
helpers.bulk(es, actions)

print("Indexing completed!")
