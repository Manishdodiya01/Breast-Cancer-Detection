# data_ingestion.py
from sklearn.datasets import load_breast_cancer
import pandas as pd

def load_dataset_into_dataframe():
    # Load Breast Cancer dataset
    datasets = load_breast_cancer()

    # Create a DataFrame from the dataset
    data = pd.DataFrame(datasets.data, columns=datasets.feature_names)
    data['target'] = datasets.target

    return data

if __name__ == "__main__":
    # If this script is run directly, load the dataset into a DataFrame
    breast_cancer_dataframe = load_dataset_into_dataframe()
    print("DataFrame created from Breast Cancer dataset:")
    print(breast_cancer_dataframe.head())

    # You can also save the DataFrame to a CSV file if needed
    # breast_cancer_dataframe.to_csv('breast_cancer_data.csv', index=False)

    # Save the DataFrame to a CSV file
    breast_cancer_dataframe.to_csv('breast_cancer_data.csv', index=False)
    print("DataFrame saved to breast_cancer_data.csv")
    
