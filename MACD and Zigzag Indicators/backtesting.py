# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from ta.trend import MACD
# from utils import base_path
# # Load data from dataset
# data = pd.read_csv(base_path / "BTCUSD_M15.csv")
# data['price'] = data['Close']  # Ensure the dataset has a column labeled 'Close'

# # Display the initial rows
# print(data.head())

# # Calculate MACD
# def calculate_macd(data):
#     macd_indicator = MACD(data['price'], window_slow=26, window_fast=12, window_sign=9)
#     data['macd'] = macd_indicator.macd()
#     data['macd_signal'] = macd_indicator.macd_signal()
#     data['macd_hist'] = macd_indicator.macd_diff()
#     return data

# # Zigzag Indicator (Custom function)
# def calculate_zigzag(data, threshold=0.02):
#     peaks, troughs = [], []
#     last_extreme = None
#     for i in range(1, len(data) - 1):
#         if data['price'].iloc[i] > data['price'].iloc[i - 1] and data['price'].iloc[i] > data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[i] - data['price'].iloc[last_extreme]) / data['price'].iloc[last_extreme] > threshold:
#                 peaks.append(i)
#                 last_extreme = i
#         elif data['price'].iloc[i] < data['price'].iloc[i - 1] and data['price'].iloc[i] < data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[last_extreme] - data['price'].iloc[i]) / data['price'].iloc[last_extreme] > threshold:
#                 troughs.append(i)
#                 last_extreme = i
#     data['peaks'] = np.nan
#     data['troughs'] = np.nan
#     data.loc[peaks, 'peaks'] = data['price']
#     data.loc[troughs, 'troughs'] = data['price']
#     return data

# # Apply the strategy
# def apply_strategy(data, initial_balance=6000, trade_amount=100):
#     balance = initial_balance
#     trades = []
    
#     for i in range(1, len(data)):
#         # MACD indicator logic
#         macd = data['macd'].iloc[i]
#         macd_signal = data['macd_signal'].iloc[i]
#         macd_hist = data['macd_hist'].iloc[i]
        
#         # Entry conditions
#         if macd < macd_signal and macd_hist < 0:
#             direction = "put"
#             entry_price = data['price'].iloc[i]
#             trades.append((data.index[i], direction, entry_price))
#             balance -= trade_amount
#         elif macd > macd_signal and macd_hist > 0:
#             direction = "call"
#             entry_price = data['price'].iloc[i]
#             trades.append((data.index[i], direction, entry_price))
#             balance -= trade_amount

#         # Evaluate trades
#         if trades:
#             last_trade = trades[-1]
#             if last_trade[1] == "put" and data['price'].iloc[i] < last_trade[2]:
#                 balance += trade_amount * 2  # Winning scenario in binary options
#             elif last_trade[1] == "call" and data['price'].iloc[i] > last_trade[2]:
#                 balance += trade_amount * 2
            
#     return balance, trades

# # Calculate indicators
# data = calculate_macd(data)
# data = calculate_zigzag(data)
# initial_balance=1000
# # Apply the strategy
# final_balance, trades = apply_strategy(data, initial_balance=initial_balance, trade_amount=10)

# # Display results
# print(f"Initial Balance: ${initial_balance}")
# print(f"Final Balance: ${final_balance}")
# print(f"Number of Trades Executed: {len(trades)}")

# # Plot the indicators and trades
# plt.figure(figsize=(14, 8))
# plt.plot(data['price'], label='Price')
# plt.plot(data['macd'], label='MACD')
# plt.plot(data['macd_signal'], label='MACD Signal')
# plt.scatter(data.index, data['peaks'], marker='^', color='green', label='Peaks')
# plt.scatter(data.index, data['troughs'], marker='v', color='red', label='Troughs')
# plt.legend()
# plt.show()



# #### Improvements
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from ta.trend import MACD
# from pathlib import Path

# # Define file paths
# base_path = Path("C:/Users/yonah/OneDrive/Documents/Trading/Binary_Options/Binary-Options/Datasets")
# data_path = base_path / "EURUSD_M15.csv"
# output_path = base_path / "Trade_Results.csv"

# # Load data from dataset
# data = pd.read_csv(data_path)
# data['price'] = data['Close']  # Using the 'Close' price as the main price column

# # Calculate MACD
# def calculate_macd(data):
#     macd_indicator = MACD(data['price'], window_slow=26, window_fast=12, window_sign=9)
#     data['macd'] = macd_indicator.macd()
#     data['macd_signal'] = macd_indicator.macd_signal()
#     data['macd_hist'] = macd_indicator.macd_diff()
#     return data

# # Calculate Zigzag indicator
# def calculate_zigzag(data, threshold=0.02):
#     peaks, troughs = [], []
#     last_extreme = None
#     for i in range(1, len(data) - 1):
#         if data['price'].iloc[i] > data['price'].iloc[i - 1] and data['price'].iloc[i] > data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[i] - data['price'].iloc[last_extreme]) / data['price'].iloc[last_extreme] > threshold:
#                 peaks.append(i)
#                 last_extreme = i
#         elif data['price'].iloc[i] < data['price'].iloc[i - 1] and data['price'].iloc[i] < data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[last_extreme] - data['price'].iloc[i]) / data['price'].iloc[last_extreme] > threshold:
#                 troughs.append(i)
#                 last_extreme = i
#     data['peaks'] = np.nan
#     data['troughs'] = np.nan
#     data.loc[peaks, 'peaks'] = data['price']
#     data.loc[troughs, 'troughs'] = data['price']
#     return data

# # Apply the strategy with risk management
# def apply_strategy(data, initial_balance=1000, trade_amount=10):
#     balance = initial_balance
#     trades = []
#     last_trade_index = -10  # Ensure no immediate trades are taken too close to each other

#     for i in range(1, len(data)):
#         macd = data['macd'].iloc[i]
#         macd_signal = data['macd_signal'].iloc[i]
#         macd_hist = data['macd_hist'].iloc[i]

#         # Filter conditions
#         in_uptrend = data['macd'].iloc[i] > data['macd_signal'].iloc[i]  # Uptrend filter
#         in_downtrend = data['macd'].iloc[i] < data['macd_signal'].iloc[i]  # Downtrend filter

#         # Entry conditions with a filter and minimal interval between trades
#         if i - last_trade_index > 10:
#             if in_downtrend and macd < macd_signal and macd_hist < 0:
#                 direction = "put"
#                 entry_price = data['price'].iloc[i]
#                 trades.append((data.index[i], direction, entry_price))
#                 balance -= trade_amount
#                 last_trade_index = i  # Update last trade index
#             elif in_uptrend and macd > macd_signal and macd_hist > 0:
#                 direction = "call"
#                 entry_price = data['price'].iloc[i]
#                 trades.append((data.index[i], direction, entry_price))
#                 balance -= trade_amount
#                 last_trade_index = i  # Update last trade index

#         # Evaluate trades
#         if trades:
#             last_trade = trades[-1]
#             if last_trade[1] == "put" and data['price'].iloc[i] < last_trade[2]:
#                 balance += trade_amount * 2  # Winning put trade
#             elif last_trade[1] == "call" and data['price'].iloc[i] > last_trade[2]:
#                 balance += trade_amount * 2  # Winning call trade

#     # Save results to CSV
#     trades_df = pd.DataFrame(trades, columns=["Index", "Direction", "Entry Price"])
#     trades_df["Balance"] = balance
#     trades_df.to_csv(output_path, index=False)

#     return balance, trades

# # Calculate indicators
# data = calculate_macd(data)
# data = calculate_zigzag(data)

# # Run strategy
# initial_balance = 1000
# final_balance, trades = apply_strategy(data, initial_balance=initial_balance, trade_amount=10)

# # Display results
# print(f"Initial Balance: ${initial_balance}")
# print(f"Final Balance: ${final_balance}")
# print(f"Number of Trades Executed: {len(trades)}")

# # Plotting
# plt.figure(figsize=(14, 8))
# plt.plot(data['price'], label='Price')
# plt.plot(data['macd'], label='MACD')
# plt.plot(data['macd_signal'], label='MACD Signal')
# plt.scatter(data.index, data['peaks'], marker='^', color='green', label='Peaks')
# plt.scatter(data.index, data['troughs'], marker='v', color='red', label='Troughs')
# plt.legend()
# plt.show()



# improvement 2

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from ta.trend import MACD
# from pathlib import Path

# # Define file paths
# base_path = Path("C:/Users/yonah/OneDrive/Documents/Trading/Binary_Options/Binary-Options/Datasets")
# data_path = base_path / "EURUSD_M15.csv"
# output_path = base_path / "Trade_Results.csv"

# # Load data from dataset
# data = pd.read_csv(data_path)
# data['price'] = data['Close']  # Using the 'Close' price as the main price column

# # Calculate MACD
# def calculate_macd(data):
#     macd_indicator = MACD(data['price'], window_slow=26, window_fast=12, window_sign=9)
#     data['macd'] = macd_indicator.macd()
#     data['macd_signal'] = macd_indicator.macd_signal()
#     data['macd_hist'] = macd_indicator.macd_diff()
#     return data

# # Calculate Zigzag indicator
# def calculate_zigzag(data, threshold=0.02):
#     peaks, troughs = [], []
#     last_extreme = None
#     for i in range(1, len(data) - 1):
#         if data['price'].iloc[i] > data['price'].iloc[i - 1] and data['price'].iloc[i] > data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[i] - data['price'].iloc[last_extreme]) / data['price'].iloc[last_extreme] > threshold:
#                 peaks.append(i)
#                 last_extreme = i
#         elif data['price'].iloc[i] < data['price'].iloc[i - 1] and data['price'].iloc[i] < data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[last_extreme] - data['price'].iloc[i]) / data['price'].iloc[last_extreme] > threshold:
#                 troughs.append(i)
#                 last_extreme = i
#     data['peaks'] = np.nan
#     data['troughs'] = np.nan
#     data.loc[peaks, 'peaks'] = data['price']
#     data.loc[troughs, 'troughs'] = data['price']
#     return data

# # Apply the strategy with risk management
# def apply_strategy(data, initial_balance=1000, trade_amount=10, win_probability=0.6):
#     balance = initial_balance
#     trades = []
#     last_trade_index = -10  # Ensure no immediate trades are taken too close to each other

#     for i in range(1, len(data)):
#         macd = data['macd'].iloc[i]
#         macd_signal = data['macd_signal'].iloc[i]
#         macd_hist = data['macd_hist'].iloc[i]

#         # Filter conditions
#         in_uptrend = data['macd'].iloc[i] > data['macd_signal'].iloc[i]  # Uptrend filter
#         in_downtrend = data['macd'].iloc[i] < data['macd_signal'].iloc[i]  # Downtrend filter

#         # Entry conditions with a filter and minimal interval between trades
#         if i - last_trade_index > 10:
#             if in_downtrend and macd < macd_signal and macd_hist < 0:
#                 direction = "put"
#                 entry_price = data['price'].iloc[i]
#                 trades.append((data.index[i], direction, entry_price))
#                 balance -= trade_amount
#                 last_trade_index = i  # Update last trade index
#             elif in_uptrend and macd > macd_signal and macd_hist > 0:
#                 direction = "call"
#                 entry_price = data['price'].iloc[i]
#                 trades.append((data.index[i], direction, entry_price))
#                 balance -= trade_amount
#                 last_trade_index = i  # Update last trade index

#         # Evaluate trades based on winning probability
#         if trades:
#             last_trade = trades[-1]
#             if np.random.rand() < win_probability:  # Simulate win/loss based on probability
#                 if last_trade[1] == "put" and data['price'].iloc[i] < last_trade[2]:
#                     balance += trade_amount * 1.8  # Winning put trade
#                 elif last_trade[1] == "call" and data['price'].iloc[i] > last_trade[2]:
#                     balance += trade_amount * 1.8  # Winning call trade
#             else:
#                 # Simulate loss on the trade
#                 continue  # No balance change, just skip to next iteration

#     # Save results to CSV
#     trades_df = pd.DataFrame(trades, columns=["Index", "Direction", "Entry Price"])
#     trades_df["Balance"] = balance
#     trades_df.to_csv(output_path, index=False)

#     return balance, trades

# # Calculate indicators
# data = calculate_macd(data)
# data = calculate_zigzag(data)

# # Run strategy
# initial_balance = 1000
# final_balance, trades = apply_strategy(data, initial_balance=initial_balance, trade_amount=10, win_probability=0.6)

# # Display results
# print(f"Initial Balance: ${initial_balance}")
# print(f"Final Balance: ${final_balance:.2f}")
# print(f"Number of Trades Executed: {len(trades)}")

# # Plotting
# plt.figure(figsize=(14, 8))
# plt.plot(data['price'], label='Price')
# plt.plot(data['macd'], label='MACD')
# plt.plot(data['macd_signal'], label='MACD Signal')
# plt.scatter(data.index, data['peaks'], marker='^', color='green', label='Peaks')
# plt.scatter(data.index, data['troughs'], marker='v', color='red', label='Troughs')
# plt.legend()
# plt.show()



# improvements 3
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from ta.trend import MACD
# from pathlib import Path
# from datetime import datetime

# # Define file paths
# base_path = Path("C:/Users/yonah/OneDrive/Documents/Trading/Binary_Options/Binary-Options/Datasets")
# data_path = base_path / "EURUSD_M15.csv"
# output_path = base_path / "Trade_Results.csv"

# # Load data from dataset
# data = pd.read_csv(data_path)
# data['price'] = data['Close']  # Using the 'Close' price as the main price column

# # Calculate MACD
# def calculate_macd(data):
#     macd_indicator = MACD(data['price'], window_slow=26, window_fast=12, window_sign=9)
#     data['macd'] = macd_indicator.macd()
#     data['macd_signal'] = macd_indicator.macd_signal()
#     data['macd_hist'] = macd_indicator.macd_diff()
#     return data

# # Calculate Zigzag indicator
# def calculate_zigzag(data, threshold=0.02):
#     peaks, troughs = [], []
#     last_extreme = None
#     for i in range(1, len(data) - 1):
#         if data['price'].iloc[i] > data['price'].iloc[i - 1] and data['price'].iloc[i] > data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[i] - data['price'].iloc[last_extreme]) / data['price'].iloc[last_extreme] > threshold:
#                 peaks.append(i)
#                 last_extreme = i
#         elif data['price'].iloc[i] < data['price'].iloc[i - 1] and data['price'].iloc[i] < data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[last_extreme] - data['price'].iloc[i]) / data['price'].iloc[last_extreme] > threshold:
#                 troughs.append(i)
#                 last_extreme = i
#     data['peaks'] = np.nan
#     data['troughs'] = np.nan
#     data.loc[peaks, 'peaks'] = data['price']
#     data.loc[troughs, 'troughs'] = data['price']
#     return data

# # Apply the strategy with correct balance updates
# def apply_strategy(data, initial_balance=1000, trade_amount=10, win_probability=0.6):
#     balance = initial_balance
#     trades = []
#     last_trade_index = -10  # Ensure no immediate trades are taken too close to each other

#     for i in range(1, len(data)):
#         macd = data['macd'].iloc[i]
#         macd_signal = data['macd_signal'].iloc[i]
#         macd_hist = data['macd_hist'].iloc[i]

#         # Filter conditions
#         in_uptrend = data['macd'].iloc[i] > data['macd_signal'].iloc[i]  # Uptrend filter
#         in_downtrend = data['macd'].iloc[i] < data['macd_signal'].iloc[i]  # Downtrend filter

#         # Entry conditions with a filter and minimal interval between trades
#         if i - last_trade_index > 10:
#             if in_downtrend and macd < macd_signal and macd_hist < 0:
#                 direction = "put"
#                 entry_price = data['price'].iloc[i]
#                 last_trade_index = i  # Update last trade index
#             elif in_uptrend and macd > macd_signal and macd_hist > 0:
#                 direction = "call"
#                 entry_price = data['price'].iloc[i]
#                 last_trade_index = i  # Update last trade index
#             else:
#                 continue

#             # Evaluate trade outcome based on win probability
#             if np.random.rand() < win_probability:
#                 # Winning trade
#                 balance += trade_amount  # Add profit equivalent to trade amount
#                 result = "win"
#             else:
#                 # Losing trade
#                 balance -= trade_amount  # Deduct trade amount for a loss
#                 result = "loss"

#             # Log each trade with time and balance
#             trade_time = data['Date'].iloc[i] if 'Date' in data.columns else datetime.now().isoformat()
#             trades.append((trade_time, data.index[i], direction, entry_price, result, balance))

#     # Save results to CSV
#     trades_df = pd.DataFrame(trades, columns=["Time", "Index", "Direction", "Entry Price", "Result", "Balance"])
#     trades_df.to_csv(output_path, index=False)

#     return balance, trades

# # Calculate indicators
# data = calculate_macd(data)
# data = calculate_zigzag(data)

# # Run strategy
# initial_balance = 1000
# final_balance, trades = apply_strategy(data, initial_balance=initial_balance, trade_amount=10, win_probability=0.6)

# # Display results
# print(f"Initial Balance: ${initial_balance}")
# print(f"Final Balance: ${final_balance:.2f}")
# print(f"Number of Trades Executed: {len(trades)}")

# # Plotting
# plt.figure(figsize=(14, 8))
# plt.plot(data['price'], label='Price')
# plt.plot(data['macd'], label='MACD')
# plt.plot(data['macd_signal'], label='MACD Signal')
# plt.scatter(data.index, data['peaks'], marker='^', color='green', label='Peaks')
# plt.scatter(data.index, data['troughs'], marker='v', color='red', label='Troughs')
# plt.legend()
# plt.show()


# improvements 4

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from ta.trend import MACD
# from pathlib import Path

# # Define file paths
# base_path = Path("C:/Users/yonah/OneDrive/Documents/Trading/Binary_Options/Binary-Options/Datasets")
# data_path = base_path / "EURUSD_M15.csv"
# output_path = base_path / "Trade_Results.csv"

# # Load data from dataset
# data = pd.read_csv(data_path)
# data['price'] = data['Close']  # Using the 'Close' price as the main price column

# # Calculate MACD
# def calculate_macd(data):
#     macd_indicator = MACD(data['price'], window_slow=26, window_fast=12, window_sign=9)
#     data['macd'] = macd_indicator.macd()
#     data['macd_signal'] = macd_indicator.macd_signal()
#     data['macd_hist'] = macd_indicator.macd_diff()
#     return data

# # Calculate Zigzag indicator
# def calculate_zigzag(data, threshold=0.02):
#     peaks, troughs = [], []
#     last_extreme = None
#     for i in range(1, len(data) - 1):
#         if data['price'].iloc[i] > data['price'].iloc[i - 1] and data['price'].iloc[i] > data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[i] - data['price'].iloc[last_extreme]) / data['price'].iloc[last_extreme] > threshold:
#                 peaks.append(i)
#                 last_extreme = i
#         elif data['price'].iloc[i] < data['price'].iloc[i - 1] and data['price'].iloc[i] < data['price'].iloc[i + 1]:
#             if last_extreme is None or (data['price'].iloc[last_extreme] - data['price'].iloc[i]) / data['price'].iloc[last_extreme] > threshold:
#                 troughs.append(i)
#                 last_extreme = i
#     data['peaks'] = np.nan
#     data['troughs'] = np.nan
#     data.loc[peaks, 'peaks'] = data['price']
#     data.loc[troughs, 'troughs'] = data['price']
#     return data

# # Apply the strategy with risk management
# def apply_strategy(data, initial_balance=1000, trade_amount=10, win_probability=0.6):
#     balance = initial_balance
#     trades = []
#     last_trade_index = -10  # Ensure no immediate trades are taken too close to each other

#     for i in range(1, len(data)):
#         macd = data['macd'].iloc[i]
#         macd_signal = data['macd_signal'].iloc[i]
#         macd_hist = data['macd_hist'].iloc[i]

#         # Filter conditions
#         in_uptrend = data['macd'].iloc[i] > data['macd_signal'].iloc[i]  # Uptrend filter
#         in_downtrend = data['macd'].iloc[i] < data['macd_signal'].iloc[i]  # Downtrend filter

#         # Entry conditions with a filter and minimal interval between trades
#         if i - last_trade_index > 10:
#             entry_time = data['Time'].iloc[i]  # Capture the entry time
#             if in_downtrend and macd < macd_signal and macd_hist < 0:
#                 direction = "put"
#                 entry_price = data['price'].iloc[i]
#                 trades.append((entry_time, data.index[i], direction, entry_price, balance))
#                 balance -= trade_amount
#                 last_trade_index = i  # Update last trade index
#             elif in_uptrend and macd > macd_signal and macd_hist > 0:
#                 direction = "call"
#                 entry_price = data['price'].iloc[i]
#                 trades.append((entry_time, data.index[i], direction, entry_price, balance))
#                 balance -= trade_amount
#                 last_trade_index = i  # Update last trade index

#         # Evaluate trades based on winning probability
#         if trades:
#             last_trade = trades[-1]
#             if np.random.rand() < win_probability:  # Simulate win/loss based on probability
#                 if last_trade[2] == "put" and data['price'].iloc[i] < last_trade[3]:
#                     balance += trade_amount * 1.8  # Winning put trade
#                 elif last_trade[2] == "call" and data['price'].iloc[i] > last_trade[3]:
#                     balance += trade_amount * 1.8  # Winning call trade

#     # Save results to CSV with entry time
#     trades_df = pd.DataFrame(trades, columns=["Time", "Index", "Direction", "Entry Price", "Balance"])
#     trades_df.to_csv(output_path, index=False)

#     return balance, trades

# # Calculate indicators
# data = calculate_macd(data)
# data = calculate_zigzag(data)

# # Run strategy
# initial_balance = 1000
# final_balance, trades = apply_strategy(data, initial_balance=initial_balance, trade_amount=10, win_probability=0.6)

# # Display results
# print(f"Initial Balance: ${initial_balance}")
# print(f"Final Balance: ${final_balance:.2f}")
# print(f"Number of Trades Executed: {len(trades)}")

# # Plotting
# plt.figure(figsize=(14, 8))
# plt.plot(data['price'], label='Price')
# plt.plot(data['macd'], label='MACD')
# plt.plot(data['macd_signal'], label='MACD Signal')
# plt.scatter(data.index, data['peaks'], marker='^', color='green', label='Peaks')
# plt.scatter(data.index, data['troughs'], marker='v', color='red', label='Troughs')
# plt.legend()
# plt.show()



# improvement 5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ta.trend import MACD
from pathlib import Path

# Define file paths
base_path = Path("C:/Users/yonah/OneDrive/Documents/Trading/Binary_Options/Binary-Options/Datasets")
data_path = base_path / "EURUSD_M15.csv"
output_path = base_path / "Trade_Results.csv"

# Load data from dataset
data = pd.read_csv(data_path)
data['price'] = data['Close']  # Using the 'Close' price as the main price column

# Calculate MACD
def calculate_macd(data):
    macd_indicator = MACD(data['price'], window_slow=26, window_fast=12, window_sign=9)
    data['macd'] = macd_indicator.macd()
    data['macd_signal'] = macd_indicator.macd_signal()
    data['macd_hist'] = macd_indicator.macd_diff()
    return data

# Calculate Zigzag indicator
def calculate_zigzag(data, threshold=0.02):
    peaks, troughs = [], []
    last_extreme = None
    for i in range(1, len(data) - 1):
        if data['price'].iloc[i] > data['price'].iloc[i - 1] and data['price'].iloc[i] > data['price'].iloc[i + 1]:
            if last_extreme is None or (data['price'].iloc[i] - data['price'].iloc[last_extreme]) / data['price'].iloc[last_extreme] > threshold:
                peaks.append(i)
                last_extreme = i
        elif data['price'].iloc[i] < data['price'].iloc[i - 1] and data['price'].iloc[i] < data['price'].iloc[i + 1]:
            if last_extreme is None or (data['price'].iloc[last_extreme] - data['price'].iloc[i]) / data['price'].iloc[last_extreme] > threshold:
                troughs.append(i)
                last_extreme = i
    data['peaks'] = np.nan
    data['troughs'] = np.nan
    data.loc[peaks, 'peaks'] = data['price']
    data.loc[troughs, 'troughs'] = data['price']
    return data

# Apply the strategy with risk management
def apply_strategy(data, initial_balance=1000, trade_amount=10, win_probability=0.6):
    balance = initial_balance
    trades = []
    last_trade_index = -10  # Ensure no immediate trades are taken too close to each other

    for i in range(1, len(data)):
        macd = data['macd'].iloc[i]
        macd_signal = data['macd_signal'].iloc[i]
        macd_hist = data['macd_hist'].iloc[i]

        # Filter conditions
        in_uptrend = data['macd'].iloc[i] > data['macd_signal'].iloc[i]  # Uptrend filter
        in_downtrend = data['macd'].iloc[i] < data['macd_signal'].iloc[i]  # Downtrend filter

        # Entry conditions with a filter and minimal interval between trades
        if i - last_trade_index > 10:
            entry_time = data['Time'].iloc[i]  # Capture the entry time
            if in_downtrend and macd < macd_signal and macd_hist < 0:
                direction = "put"
                entry_price = data['price'].iloc[i]
                last_trade_index = i  # Update last trade index
                
                # Simulate win/loss and adjust balance
                if np.random.rand() < win_probability:  # Simulate win
                    result = "win"
                    balance += trade_amount * 0.8  # 80% profit on win
                else:  # Simulate loss
                    result = "loss"
                    balance -= trade_amount  # Full loss on loss

                trades.append((entry_time, data.index[i], direction, entry_price, result, balance))
                
            elif in_uptrend and macd > macd_signal and macd_hist > 0:
                direction = "call"
                entry_price = data['price'].iloc[i]
                last_trade_index = i  # Update last trade index

                # Simulate win/loss and adjust balance
                if np.random.rand() < win_probability:  # Simulate win
                    result = "win"
                    balance += trade_amount * 0.8  # 80% profit on win
                else:  # Simulate loss
                    result = "loss"
                    balance -= trade_amount  # Full loss on loss

                trades.append((entry_time, data.index[i], direction, entry_price, result, balance))

    # Save results to CSV with entry time
    trades_df = pd.DataFrame(trades, columns=["Time", "Index", "Direction", "Entry Price", "Result", "Balance"])
    trades_df.to_csv(output_path, index=False)

    return balance, trades

# Calculate indicators
data = calculate_macd(data)
data = calculate_zigzag(data)

# Run strategy
initial_balance = 1000
final_balance, trades = apply_strategy(data, initial_balance=initial_balance, trade_amount=10, win_probability=0.6)

# Display results
print(f"Initial Balance: ${initial_balance}")
print(f"Final Balance: ${final_balance:.2f}")
print(f"Number of Trades Executed: {len(trades)}")

# Plotting
plt.figure(figsize=(14, 8))
plt.plot(data['price'], label='Price')
plt.plot(data['macd'], label='MACD')
plt.plot(data['macd_signal'], label='MACD Signal')
plt.scatter(data.index, data['peaks'], marker='^', color='green', label='Peaks')
plt.scatter(data.index, data['troughs'], marker='v', color='red', label='Troughs')
plt.legend()
plt.show()
