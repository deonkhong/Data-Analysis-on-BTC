# Data-Analysis-on-BTC (CAA 18-11-23)

## Analysis Overview
This project presents a statistical analysis of Bitcoin's performance over different timeframes. The analysis includes average gains and losses, along with their standard deviations, across daily, weekly, and monthly periods.

### Daily Timeframe
- **Average Daily Gain:** 2.49%
- **Standard Deviation of Daily Gains:** 2.79%
- **Average Daily Loss:** −2.37%
- **Standard Deviation of Daily Losses:** 2.83%

### Weekly Timeframe
- **Average Weekly Gain:** 7.91%
- **Standard Deviation of Weekly Gains:** 7.26%
- **Average Weekly Loss:** −6.59%
- **Standard Deviation of Weekly Losses:** 6.63%

### Monthly Timeframe
- **Average Monthly Gain:** 21.81%
- **Standard Deviation of Monthly Gains:** 16.60%
- **Average Monthly Loss:** −12.67%
- **Standard Deviation of Monthly Losses:** 9.67%

# Moving Averages and Volatility Analysis

## Moving Averages
This section outlines the Simple Moving Averages (SMA) and Exponential Moving Averages (EMA) for the latest 30-day and 90-day periods.

- **Latest 30-Day Simple Moving Average (SMA):** $34,855.44
- **Latest 90-Day Simple Moving Average (SMA):** $29,447.64
- **Latest 30-Day Exponential Moving Average (EMA):** $34,580.95
- **Latest 90-Day Exponential Moving Average (EMA):** $31,189.41

## Volatility Analysis
Volatility is measured as the standard deviation over the 30-day and 90-day periods.

- **Latest 30-Day Volatility:** $2,048.84
- **Latest 90-Day Volatility:** $4,074.94

## Sharpe Ratio
The Sharpe Ratio provides a measure for calculating the return of an investment compared to its risk.

- **Annualized Sharpe Ratio:** 0.86

# Bitcoin Time Series Analysis

## Autocorrelation Analysis
This section examines the autocorrelation at different lags to understand the serial correlations in Bitcoin's daily returns.

- **Autocorrelation (Lag 1):** -0.018
  - Negative autocorrelation at a lag of 1 day suggests a slight tendency towards mean-reversion over very short periods.
- **Autocorrelation (Lag 5):** 0.008
  - Very slight positive autocorrelation at a lag of 5 days.
- **Autocorrelation (Lag 10):** 0.038
  - Slight positive autocorrelation at a lag of 10 days.
  
The results indicate weak serial correlations, with negative autocorrelation at lag 1 and slight positive autocorrelation at higher lags.

## Hurst Exponent
- **Hurst Exponent:** NaN
  - The undefined value (NaN) typically results from numerical issues in the calculation, especially in shorter or less variable time series. The Hurst Exponent assesses the long-term memory of time series, indicating whether it's mean-reverting, trending, or random.

## Value at Risk (VaR)
- **Value at Risk (95%):** -5.76%
  - This implies there is a 95% chance that Bitcoin will not lose more than 5.76% of its value in a single day.

## Skewness and Kurtosis
- **Skewness:** -0.14
  - Indicates slight negative skewness in the distribution.
- **Kurtosis:** 7.52
  - A leptokurtic distribution, suggesting a higher probability of extreme values compared to a normal distribution.
