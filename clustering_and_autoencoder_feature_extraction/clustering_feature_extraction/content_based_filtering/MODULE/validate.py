# import required libraries
import numpy as np
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor

class evaluation():
    ''' This class performs the kfold cross validation for the given dataset.

    Input:
    - n_estimators: Number of tress in random forest  regressor model
    - X: training dataset without labels
    - y: dataset with labels only
    
    Output: Return predictions and truth values 
    '''
    def __init__(self, X, y, k, n_estimators, min_rating=1, max_rating=5):
        self.X, self.y, self.k, self.n_estimators, self.min_rating, self.max_rating = \
            X, y, k, n_estimators, min_rating, max_rating

    def kfold(self):
        self.kfold = KFold(n_splits=self.k, shuffle=True, random_state=32)
        classes, truth_val = [], []
        for i, (train_index, test_index) in enumerate(self.kfold.split(self.X, self.y)):
            print(f'Fold {i+1}:')
            # define model 
            rf_model = RandomForestRegressor(n_estimators = self.n_estimators)
            # model fit
            rf_model.fit(self.X[train_index],self.y[train_index])
            # model predict
            predict = rf_model.predict(self.X[test_index])
            # scale ratings to orignal value
            x =  (predict * (self.max_rating - self.min_rating) ) + self.min_rating
            # append predictions and real values
            classes.append(x)
            truth = self.y[test_index]
            truth_val.append(truth)
        # convert list to array
        classes = np.array(classes)
        truth_val = np.array(truth_val)
        return classes, truth_val


