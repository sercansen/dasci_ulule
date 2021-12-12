from pandas import DataFrame
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import numpy as np
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import seaborn as sns

from utils.utils import get_html_from_fig


def prep_data_ml(data):
    df = data.drop(columns=['goal_raised', 'amount_raised', 'comments_count', 'fans_count', 'id', 'percent', 'supporters_count', 'type'])
    X_train, X_test, y_train, y_test = train_test_split(df, data['goal_raised'])
    X_train = StandardScaler().fit_transform(X_train.values)
    X_test = StandardScaler().fit_transform(X_test.values)
    return X_train, X_test, y_train, y_test

def confusion_matrix(y_test, y_preds):
	cnf_matrix = metrics.confusion_matrix(y_test, y_preds)

	class_names=[0,1] # name  of classes
	fig, ax = plt.subplots()
	tick_marks = np.arange(len(class_names))
	plt.xticks(tick_marks, class_names)
	plt.yticks(tick_marks, class_names)
	# create heatmap
	sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
	ax.xaxis.set_label_position("top")
	plt.tight_layout()
	plt.title('Confusion matrix', y=1.1)
	plt.ylabel('Actual label')
	plt.xlabel('Predicted label')

	res = get_html_from_fig(fig)
	plt.close()

	return res

def roc_curve(X_test, y_test, log_reg_model):
	y_pred_proba = log_reg_model.predict_proba(X_test)[::,1]
	fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
	auc = metrics.roc_auc_score(y_test, y_pred_proba)
	fig, ax = plt.subplots()
	plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
	plt.legend(loc=4)

	res = get_html_from_fig(fig)
	plt.close()

	return res