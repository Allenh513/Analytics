from sklearn import metrics
import numpy as np

def regression_measures_of_fit(y_true,y_pred):
    explained_var = metrics.explained_variance_score(y_true,y_pred)
    mean_absolute_err = metrics.mean_absolute_error(y_true,y_pred)
    mean_square_err = metrics.mean_squared_error(y_true,y_pred)
    r_mean_square_err = np.sqrt(mean_square_err)
    r_square = metrics.r2_score(y_true,y_pred)

    return dict(
        {
            'explained_variance':explained_var,
            'MAE':mean_absolute_err,
            'MSE':mean_square_err,
            'RMSE':r_mean_square_err,
            'R2':r_square
         }
    )