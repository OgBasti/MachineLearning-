import pandas as pd

def feature_engineering(X):
    '''Ensures data is as designed. Column State was not selected'''
    numerical_features = [
    "Account length", "Area code", "Number vmail messages", 
    "Total day minutes", "Total day calls", "Total day charge", 
    "Total eve minutes", "Total eve calls", "Total eve charge", 
    "Total night minutes", "Total night calls", "Total night charge", 
    "Total intl minutes", "Total intl calls", "Total intl charge", 
    "Customer service calls"
    ]

    categorical_features = ["International plan", "Voice mail plan"]

    X = pd.DataFrame(X, columns=numerical_features + categorical_features)
    
    # Drop the 'Churn' column if it exists
    if 'Churn' in X.columns:
        X = X.drop(columns=['Churn'], errors='ignore')
    
    # Create a new feature for total service usage
    X["Total_Service_Usage"] = (
        X["Total day minutes"] + 
        X["Total eve minutes"] + 
        X["Total night minutes"] +
        X["Total intl minutes"] 
        )
    
    # Create a new feature for total charges
    X["Total_Rate"] = (
        X["Total day charge"] + 
        X["Total eve charge"] + 
        X["Total night charge"] + 
        X["Total intl charge"]
        )

    return X




import pandas as pd



