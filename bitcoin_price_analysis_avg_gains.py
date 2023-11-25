
import pandas as pd

# Load the dataset
file_path = 'BTC-USD.csv'  # Update the file path as needed
btc_data = pd.read_csv(file_path)

# Calculate daily price change and percentage change
btc_data['Price Change'] = btc_data['Close'].diff()
btc_data['Percent Change'] = btc_data['Price Change'] / btc_data['Close'].shift(1) * 100

# Separate daily gains and losses
daily_gains = btc_data[btc_data['Percent Change'] > 0]['Percent Change']
daily_losses = btc_data[btc_data['Percent Change'] < 0]['Percent Change']

# Calculate average and standard deviation for daily gains and losses
average_daily_gain = daily_gains.mean()
std_dev_daily_gain = daily_gains.std()
average_daily_loss = daily_losses.mean()
std_dev_daily_loss = daily_losses.std()

# Convert 'Date' to datetime and set it as index for monthly calculations
btc_data['Date'] = pd.to_datetime(btc_data['Date'])
btc_data.set_index('Date', inplace=True)

# Resample to get end-of-month prices and calculate monthly percent change
btc_monthly = btc_data['Close'].resample('M').last().pct_change() * 100

# Separate monthly gains and losses
monthly_gains = btc_monthly[btc_monthly > 0]
monthly_losses = btc_monthly[btc_monthly < 0]

# Calculate average and standard deviation for monthly gains and losses
average_monthly_gain = monthly_gains.mean()
std_dev_monthly_gain = monthly_gains.std()
average_monthly_loss = monthly_losses.mean()
std_dev_monthly_loss = monthly_losses.std()

# Print results
print("Daily Analysis:")
print("Average Daily Gain:", average_daily_gain, "%")
print("Standard Deviation of Daily Gains:", std_dev_daily_gain, "%")
print("Average Daily Loss:", average_daily_loss, "%")
print("Standard Deviation of Daily Losses:", std_dev_daily_loss, "%")
print("\nMonthly Analysis:")
print("Average Monthly Gain:", average_monthly_gain, "%")
print("Standard Deviation of Monthly Gains:", std_dev_monthly_gain, "%")
print("Average Monthly Loss:", average_monthly_loss, "%")
print("Standard Deviation of Monthly Losses:", std_dev_monthly_loss, "%")

# Weekly Analysis
# Resample to get end-of-week prices and calculate weekly percent change
btc_weekly = btc_data['Close'].resample('W').last().pct_change() * 100

# Separate weekly gains and losses
weekly_gains = btc_weekly[btc_weekly > 0]
weekly_losses = btc_weekly[btc_weekly < 0]

# Calculate average and standard deviation for weekly gains and losses
average_weekly_gain = weekly_gains.mean()
std_dev_weekly_gain = weekly_gains.std()
average_weekly_loss = weekly_losses.mean()
std_dev_weekly_loss = weekly_losses.std()

# Print results for weekly analysis
print("\nWeekly Analysis:")
print("Average Weekly Gain:", average_weekly_gain, "%")
print("Standard Deviation of Weekly Gains:", std_dev_weekly_gain, "%")
print("Average Weekly Loss:", average_weekly_loss, "%")
print("Standard Deviation of Weekly Losses:", std_dev_weekly_loss, "%")


import numpy as np

# Calculating Simple Moving Averages (SMA) - 30 days and 90 days
btc_data['SMA_30'] = btc_data['Close'].rolling(window=30).mean()
btc_data['SMA_90'] = btc_data['Close'].rolling(window=90).mean()

# Calculating Exponential Moving Averages (EMA) - 30 days and 90 days
btc_data['EMA_30'] = btc_data['Close'].ewm(span=30, adjust=False).mean()
btc_data['EMA_90'] = btc_data['Close'].ewm(span=90, adjust=False).mean()

# Volatility Analysis - 30 days and 90 days rolling standard deviation
btc_data['Volatility_30'] = btc_data['Close'].rolling(window=30).std()
btc_data['Volatility_90'] = btc_data['Close'].rolling(window=90).std()

# Sharpe Ratio (Annualized)
# Assuming a risk-free rate of 0 for simplicity
risk_free_rate = 0.0
daily_returns = btc_data['Close'].pct_change()
sharpe_ratio_annualized = np.sqrt(252) * daily_returns.mean() / daily_returns.std()

# Extracting the last values of the calculated metrics for reporting
latest_sma_30 = btc_data['SMA_30'].iloc[-1]
latest_sma_90 = btc_data['SMA_90'].iloc[-1]
latest_ema_30 = btc_data['EMA_30'].iloc[-1]
latest_ema_90 = btc_data['EMA_90'].iloc[-1]
latest_volatility_30 = btc_data['Volatility_30'].iloc[-1]
latest_volatility_90 = btc_data['Volatility_90'].iloc[-1]

advanced_stats = {
    "Latest 30-Day SMA": latest_sma_30,
    "Latest 90-Day SMA": latest_sma_90,
    "Latest 30-Day EMA": latest_ema_30,
    "Latest 90-Day EMA": latest_ema_90,
    "Latest 30-Day Volatility": latest_volatility_30,
    "Latest 90-Day Volatility": latest_volatility_90,
    "Annualized Sharpe Ratio": sharpe_ratio_annualized
}

advanced_stats

from statsmodels.tsa.stattools import adfuller, kpss
from scipy.stats import skew, kurtosis

# Autocorrelation Analysis
btc_autocorr_lag1 = daily_returns.autocorr(lag=1)
btc_autocorr_lag5 = daily_returns.autocorr(lag=5)
btc_autocorr_lag10 = daily_returns.autocorr(lag=10)

# Hurst Exponent
def hurst_exponent(time_series):
    """Returns the Hurst Exponent of the time series."""
    lags = range(2, 100)
    tau = [np.sqrt(np.std(np.subtract(time_series[lag:], time_series[:-lag]))) for lag in lags]
    poly = np.polyfit(np.log(lags), np.log(tau), 1)
    return poly[0] * 2.0

hurst_exp = hurst_exponent(daily_returns.dropna())

# Value at Risk (VaR) - Historical Method (95% Confidence)
var_95 = np.percentile(daily_returns.dropna(), 5)  # Using 5% percentile since it's a left-tail measure

# Skewness and Kurtosis
skewness = skew(daily_returns.dropna())
kurt = kurtosis(daily_returns.dropna(), fisher=True)  # Fisher's definition (normal == 0.0)

# Combining the results
advanced_stats.update({
    "Autocorrelation (Lag 1)": btc_autocorr_lag1,
    "Autocorrelation (Lag 5)": btc_autocorr_lag5,
    "Autocorrelation (Lag 10)": btc_autocorr_lag10,
    "Hurst Exponent": hurst_exp,
    "Value at Risk (95%)": var_95,
    "Skewness": skewness,
    "Kurtosis": kurt
})

advanced_stats

