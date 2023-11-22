from sklearn.svm import SVC
from sklearn.metrics import accuracy_score , classification_report
import joblib


def train_model(X_train,y_train):

    # create a support vector machine classifier

    model = SVC(kernel='linear' , random_state=42)

    model.fit(X_train,y_train)

    return model

def evaluate_model(model,X_test,y_test):

    y_pred = model.predict(X_test)

    # evaluate the model

    accuracy = accuracy_score(y_pred=y_pred , y_true=y_test)
    report = classification_report(y_pred=y_pred , y_true=y_test)


    print("Model Evaluation:")
    print(f"Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)

    return accuracy


def save_model(model,model_filename='svm_model.joblib'):

    # save the trained model to a file

    joblib.dump(model,model_filename)
    print(f"Model saved to {model_filename}")


if __name__ == "__main__":
    # If this script is run directly, load the transformed data and train the model
    from data_trasformation import perform_data_transformation
    from data_ingestion import load_dataset_into_dataframe

    breast_cancer_dataframe = load_dataset_into_dataframe()
    transformed_data = perform_data_transformation(breast_cancer_dataframe)

    # Train the model
    trained_model = train_model(transformed_data['X_train'], transformed_data['y_train'])

    # Evaluate the model
    accuracy = evaluate_model(trained_model, transformed_data['X_test'], transformed_data['y_test'])

    # Save the trained model
    save_model(trained_model)