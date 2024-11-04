# import MetaTrader5 as mt5
# import pandas as pd
# import numpy as np
# import time
# from datetime import datetime
# from ta.trend import MACD

# # MetaTrader 5 setup
# if not mt5.initialize():
#     print("MetaTrader5 initialization failed")
#     quit()

# # Strategy parameters
# SYMBOL = "EURUSD"
# TRADE_AMOUNT = 10.0  # Adjust this to desired trade size
# WIN_MULTIPLIER = 1.8
# LOSE_MULTIPLIER = 1.0
# TRADE_INTERVAL = 60  # Interval between trades in seconds

# # Initialize trade logging
# output_path = "live_trade_results.csv"
# columns = ["Time", "Direction", "Entry Price", "Result", "Balance"]
# results = pd.DataFrame(columns=columns)

# # Define strategy logic functions
# def get_macd(price_data):
#     macd_indicator = MACD(price_data['close'], window_slow=26, window_fast=12, window_sign=9)
#     return macd_indicator.macd(), macd_indicator.macd_signal(), macd_indicator.macd_diff()

# def place_trade(symbol, direction, trade_amount):
#     order_type = mt5.ORDER_TYPE_BUY if direction == "call" else mt5.ORDER_TYPE_SELL
#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": trade_amount,
#         "type": order_type,
#         "price": mt5.symbol_info_tick(symbol).ask if direction == "call" else mt5.symbol_info_tick(symbol).bid,
#         "deviation": 10,
#         "magic": 234000,
#         "comment": "Automated trade",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }
#     result = mt5.order_send(request)
#     return result

# # Main loop for live trading
# balance = 1000  # Initial balance
# while True:
#     # Get latest price data
#     rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 50)  # Use M1 timeframe for real-time
#     data = pd.DataFrame(rates)
#     data['time'] = pd.to_datetime(data['time'], unit='s')

#     # Calculate MACD
#     macd, macd_signal, macd_hist = get_macd(data)

#     # Determine trade direction
#     direction = None
#     if macd.iloc[-1] > macd_signal.iloc[-1] and macd_hist.iloc[-1] > 0:
#         direction = "call"
#     elif macd.iloc[-1] < macd_signal.iloc[-1] and macd_hist.iloc[-1] < 0:
#         direction = "put"

#     if direction:
#         # Execute trade
#         trade_result = place_trade(SYMBOL, direction, TRADE_AMOUNT)
#         entry_price = mt5.symbol_info_tick(SYMBOL).ask if direction == "call" else mt5.symbol_info_tick(SYMBOL).bid
#         print(f"Trade executed: {direction} at {entry_price}")

#         # Wait and evaluate outcome
#         time.sleep(TRADE_INTERVAL)
#         exit_price = mt5.symbol_info_tick(SYMBOL).bid if direction == "call" else mt5.symbol_info_tick(SYMBOL).ask
#         result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"
        
#         # Update balance based on trade result
#         if result == "win":
#             balance += TRADE_AMOUNT * WIN_MULTIPLIER
#         else:
#             balance -= TRADE_AMOUNT * LOSE_MULTIPLIER

#         # Log trade result
#         # results = results.append({
#         #     "Time": datetime.now(),
#         #     "Direction": direction,
#         #     "Entry Price": entry_price,
#         #     "Result": result,
#         #     "Balance": balance
#         # }, ignore_index=True)
#         new_row = pd.DataFrame([{
#             "Time": datetime.now(),
#             "Direction": direction,
#             "Entry Price": entry_price,
#             "Result": result,
#             "Balance": balance
#         }])

#         results = pd.concat([results, new_row], ignore_index=True)

#         # Save to CSV
#         results.to_csv(output_path, index=False)

#         # Print current balance
#         print(f"Balance after trade: ${balance:.2f}")
        
#     # Wait a bit before the next check
#     time.sleep(10)

# # # Shutdown MetaTrader 5 connection
# # mt5.shutdown()



# after

import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
from datetime import datetime
from ta.trend import MACD

# MetaTrader 5 setup
if not mt5.initialize():
    print("MetaTrader5 initialization failed")
    quit()

# Strategy parameters
SYMBOL = "EURUSD"
TRADE_AMOUNT = 10.0  # Adjust this to desired trade size
WIN_MULTIPLIER = 1.8
LOSE_MULTIPLIER = 1.0
TRADE_INTERVAL = 60  # Interval between trades in seconds

# Initialize trade logging
output_path = "live_trade_results_2.csv"
columns = ["Time", "Direction", "Entry Price", "Exit Price", "Result", "Balance"]
results = pd.DataFrame(columns=columns)

# Define strategy logic functions
def get_macd(price_data):
    macd_indicator = MACD(price_data['close'], window_slow=26, window_fast=12, window_sign=9)
    return macd_indicator.macd(), macd_indicator.macd_signal(), macd_indicator.macd_diff()

def place_trade(symbol, direction, trade_amount):
    order_type = mt5.ORDER_TYPE_BUY if direction == "call" else mt5.ORDER_TYPE_SELL
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": trade_amount,
        "type": order_type,
        "price": mt5.symbol_info_tick(symbol).ask if direction == "call" else mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": 234000,
        "comment": "Automated trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    return result

# Main loop for live trading
balance = 1000  # Initial balance
while True:
    # Get latest price data
    rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 50)  # Use M1 timeframe for real-time
    data = pd.DataFrame(rates)
    data['time'] = pd.to_datetime(data['time'], unit='s')

    # Calculate MACD
    macd, macd_signal, macd_hist = get_macd(data)

    # Determine trade direction
    direction = None
    if macd.iloc[-1] > macd_signal.iloc[-1] and macd_hist.iloc[-1] > 0:
        direction = "call"
    elif macd.iloc[-1] < macd_signal.iloc[-1] and macd_hist.iloc[-1] < 0:
        direction = "put"

    if direction:
        # Execute trade
        trade_result = place_trade(SYMBOL, direction, TRADE_AMOUNT)
        entry_price = mt5.symbol_info_tick(SYMBOL).ask if direction == "call" else mt5.symbol_info_tick(SYMBOL).bid
        print(f"Trade executed: {direction} at {entry_price}")

        # Wait and evaluate outcome
        time.sleep(TRADE_INTERVAL)
        exit_price = mt5.symbol_info_tick(SYMBOL).bid if direction == "call" else mt5.symbol_info_tick(SYMBOL).ask
        result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"
        
        # Update balance based on trade result
        if result == "win":
            balance += TRADE_AMOUNT * WIN_MULTIPLIER
        else:
            balance -= TRADE_AMOUNT * LOSE_MULTIPLIER

        # Log trade result with Entry and Exit prices
        new_row = pd.DataFrame([{
            "Time": datetime.now(),
            "Direction": direction,
            "Entry Price": entry_price,
            "Exit Price": exit_price,
            "Result": result,
            "Balance": balance
        }])

        results = pd.concat([results, new_row], ignore_index=True)

        # Save to CSV
        results.to_csv(output_path, index=False)

        # Print current balance
        print(f"Balance after trade: ${balance:.2f}")
        
    # Wait a bit before the next check
    time.sleep(10)

# Shutdown MetaTrader 5 connection
# mt5.shutdown()
