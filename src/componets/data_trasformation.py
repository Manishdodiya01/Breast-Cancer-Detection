from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



def perform_data_transformation(data):

    X = data.drop('target' , axis=1)
    y = data['target']


    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    # return transformed_data 
    transformed_data = {
        'X_train' : X_train_scaled,
        'X_test' : X_test_scaled,
        'y_train' : y_train,
        'y_test' : y_test
        }
    
    return transformed_data



if __name__ == "__main__":

    from data_ingestion import load_dataset_into_dataframe

    breast_cancer_dataframe = load_dataset_into_dataframe()
    transformed_data = perform_data_transformation(breast_cancer_dataframe)


    print("Transformed Data:")
    print("X_train shape:", transformed_data['X_train'].shape)
    print("X_test shape:", transformed_data['X_test'].shape)
    print("y_train shape:", transformed_data['y_train'].shape)
    print("y_test shape:", transformed_data['y_test'].shape)

        