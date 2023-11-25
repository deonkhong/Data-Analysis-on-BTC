
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
