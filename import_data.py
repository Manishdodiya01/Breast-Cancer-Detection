# import_data.py
from sklearn.datasets import load_breast_cancer
from pymongo import MongoClient
import pandas as pd


def load_dataset():
    # Load Breast Cancer dataset
    datasets = load_breast_cancer()

    # Prepare data for MongoDB insertion
    data = pd.DataFrame(datasets.data, columns=datasets.feature_names)
    data['target'] = datasets.target

    return data

def insert_data_into_mongodb(data, database_name='ml_project', collection_name='breast_cancer', mongo_client_uri=None):
    # Connect to MongoDB Atlas
    client = MongoClient(mongo_client_uri)
    db = client[database_name]
    collection = db[collection_name]

    # Convert DataFrame to dictionary
    data_dict = data.to_dict(orient='records')

    # Insert data into MongoDB
    result = collection.insert_many(data_dict)
    print(f"Data inserted into MongoDB with IDs: {result.inserted_ids}")

if __name__ == "__main__":
    # If this script is run directly, load the dataset and insert into MongoDB
    mongo_client_uri = "mongodb+srv://dodiyamanish400:manish@cluster2.psi0gzw.mongodb.net/?retryWrites=true&w=majority"
    breast_cancer_data = load_dataset()
    insert_data_into_mongodb(breast_cancer_data, mongo_client_uri=mongo_client_uri)
