from pandas import DataFrame
import pandas as pd

def prep_data_ml(data: Dataframe):
	df = data.drop(columns=['goal_raised', 'amount_raised', 'comments_count', 'fans_count', 'id', 'percent', 'supporters_count', 'type'])
    X_train, X_test, y_train, y_test = train_test_split(df, data['goal_raised'])
    X_train = StandardScaler().fit_transform(X_train.values)
    X_test = StandardScaler().fit_transform(X_test.values)
    return X_train, X_test, y_train, y_test