import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error  

class result():
    ''' This class is defines compute the mean squared error and mean absolute errror 
       for kfold cross validation. The function 'validate' prints the results for kfold
    
       Input:
        - classes: numpy array of predictions from a regressor model
        - truth_val: labels for the trained model

        Output:
        print the mean and standard deviation for root mean square error 
        and mean absolute error
    '''
    def __init__(self, classes, truth_val):
        self.classes = classes
        self.truth_val = truth_val
    
    def validate(self):
        # lists with rmse and mae of kfolds
        rmse, mae = [], []
        for i in range(5):
        # root mean square error
            rmse_val = mean_squared_error(self.truth_val[i], self.classes[i], squared = False)
            # mean absolute error
            mae_val = mean_absolute_error(self.truth_val[i], self.classes[i])
            # append rmse and and mae
            rmse.append(rmse_val)
            mae.append(mae_val)
        # print mean and standard deviation for rmse and mae
        print('Metric | Mean | Standard Deviation')
        print(f'RMSE {np.mean(rmse)}, {np.std(rmse)}')
        print(f'MAE {np.mean(mae)}, {np.std(mae)}')