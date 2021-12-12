from joblib import dump, load
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
import os

def log_reg(X_train, X_test, y_train, y_test):
	if os.path.isfile("./ml_models/saved_models/logreg.joblib"):
		log_reg_model = load('./ml_models/saved_models/logreg.joblib')
	else:
		# defining parameter range
		param_grid = {'solver': ['newton-cg', 'lbfgs', 'liblinear'],
		              'penalty': ['l2'],
		              'C': [100, 10, 1.0, 0.1, 0.01]}
		 
		grid = GridSearchCV(LogisticRegression(), param_grid, refit = True, cv=4, n_jobs=-1, verbose = 1)
		 
		# fitting the model for grid search
		grid.fit(X_train, y_train)
		log_reg_model = grid.best_estimator_
		dump(log_reg_model, './ml_models/saved_models/logreg.joblib')
	
	log_reg_preds = log_reg_model.predict(X_test)
	return log_reg_model, log_reg_preds, "<p>Le score de la regression logistique après tuning des paramètres est " + str(log_reg_model.score(X_test, y_test)) + ". Avec les paramètres: solver = " + log_reg_model.solver + ", penalty = l2 et C = " + str(log_reg_model.C) + "</p>"

