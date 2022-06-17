import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.holtwinters.model import ExponentialSmoothing,TimeSeriesModel,SimpleExpSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose


class LINEAR_FORECAST:
    def arima_forecast(self,p,d,q,data,period,forecast_n_periods,metric):
        arima = ARIMA(endog=data,order=(p,d,q))
        fit_model = arima.fit()
        forecast = fit_model.forecast(steps=forecast_n_periods, alpha=0.05)
        f = pd.DataFrame(forecast)
        f.to_excel('ftest.xlsx')
        df = pd.DataFrame(data).rename(columns={metric:'final'})
        fdf = pd.DataFrame(forecast).rename(columns={'predicted_mean':'final'})
        out = pd.concat([df,fdf])
        return out

    def exp_smooth(self, data,forecast_n_periods):
        smoother = ExponentialSmoothing(endog=data)
        fit = smoother.fit()
        forecast = fit.forecast(steps=forecast_n_periods)



