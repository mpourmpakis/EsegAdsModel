import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_validate,train_test_split
from sklearn.metrics import mean_absolute_error, make_scorer

def load_data():
    """
    Loads complete dataset as dataframe
    """
    # get path to complete dataset
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'data',
                        'data.csv')

    # pandas DataFrame object
    df = pd.read_csv(path)

    return df

def split(df):
    # Inputs and Target
    y= df['DFT'].values
    x=df[['ΔCE/CN','ΔBE/CNads','ΔWS','ΔEA']].values
    
    # Splits the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(x,y, train_size=0.85, shuffle=True,random_state=91)
    
    return X_train, X_test, y_train, y_test   


def eseg_ads_model(df):
    """
    Developing the model 
    """
    X_train, X_test, y_train, y_test = split(df)
    # create standard scaler
    scaler = StandardScaler()

    # NN MLP Eseg model with tuned hyperparameters 
    nn_mlp = MLPRegressor(activation='tanh',alpha=0.112,hidden_layer_sizes=(90,80,60,40), random_state=1, solver='adam',
    learning_rate_init=0.011,max_iter=900,
    epsilon=10**(-8),n_iter_no_change=35,tol=10**(-5))

    # create model pipeline 
    model = Pipeline(steps = [
                                ('StandardScaler', scaler),
                                ('NN MLP', nn_mlp)])

    # training and returning the model
    model.fit(X_train, y_train)
    

    return model


def evaluate_error(model,df):
    mae= make_scorer(mean_absolute_error)
    X_train, X_test, y_train, y_test = split(df)
    #5-Fold Cross Validation
    cv=5  
    scores = cross_validate(model,X_train, y_train, scoring= mae,cv = cv,return_train_score=True)
    train_mae =scores['train_score'].mean()
    validation_mae=scores['test_score'].mean()
    test_mae=mae(model,X_test,y_test)
    return train_mae, validation_mae, test_mae

if __name__ == "__main__":
    df = load_data()
    model= eseg_ads_model(df)
    train_mae, validation_mae, test_mae = evaluate_error(model,df)
    print(f'Train MAE: {train_mae} eV\nValidation MAE: {validation_mae} eV\nTest MAE: {test_mae} eV')