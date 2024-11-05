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



# # after

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
# output_path = "live_trade_results_2.csv"
# columns = ["Time", "Direction", "Entry Price", "Exit Price", "Result", "Balance"]
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
# balance = 1348  # Initial balance
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

#         # Log trade result with Entry and Exit prices
#         new_row = pd.DataFrame([{
#             "Time": datetime.now(),
#             "Direction": direction,
#             "Entry Price": entry_price,
#             "Exit Price": exit_price,
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

# # Shutdown MetaTrader 5 connection
# # mt5.shutdown()


# # upgrade
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
# output_path = "live_trade_results3.csv"
# columns = ["Time", "Direction", "Entry Price", "Exit Price", "Price Difference", "Result", "Balance"]
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
#         price_difference = exit_price - entry_price
#         result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"
        
#         # Update balance based on trade result
#         if result == "win":
#             balance += TRADE_AMOUNT * WIN_MULTIPLIER
#         else:
#             balance -= TRADE_AMOUNT * LOSE_MULTIPLIER

#         # Log trade result with Entry and Exit prices and Price Difference
#         new_row = pd.DataFrame([{
#             "Time": datetime.now(),
#             "Direction": direction,
#             "Entry Price": entry_price,
#             "Exit Price": exit_price,
#             "Price Difference": price_difference,
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

# # Shutdown MetaTrader 5 connection
# # mt5.shutdown()



# # robust trading
# import MetaTrader5 as mt5
# import pandas as pd
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
# output_path = "live_trade_results4.csv"
# columns = ["Time", "Direction", "Entry Price", "Exit Price", "Price Difference", "Result", "Balance"]
# results = pd.DataFrame(columns=columns)

# # Define strategy logic functions
# def get_macd(price_data):
#     macd_indicator = MACD(price_data['close'], window_slow=26, window_fast=12, window_sign=9)
#     return macd_indicator.macd(), macd_indicator.macd_signal(), macd_indicator.macd_diff()

# def place_trade(symbol, direction, trade_amount):
#     order_type = mt5.ORDER_TYPE_BUY if direction == "call" else mt5.ORDER_TYPE_SELL
#     price = mt5.symbol_info_tick(symbol).ask if direction == "call" else mt5.symbol_info_tick(symbol).bid
#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": trade_amount,
#         "type": order_type,
#         "price": price,
#         "deviation": 10,
#         "magic": 234000,
#         "comment": "Automated trade",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }


#     result = mt5.order_send(request)
#     if result.retcode == mt5.TRADE_RETCODE_DONE:
#         return result.order, price  # Return order ID and entry price
#     else:
#         print(f"Trade execution failed: {result.retcode} and comment: {result.comment}")
#         return None, None

# def close_trade(order_id, direction):
#     position_type = mt5.ORDER_TYPE_SELL if direction == "call" else mt5.ORDER_TYPE_BUY
#     price = mt5.symbol_info_tick(SYMBOL).bid if direction == "call" else mt5.symbol_info_tick(SYMBOL).ask
#     close_request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": SYMBOL,
#         "volume": TRADE_AMOUNT,
#         "type": position_type,
#         "position": order_id,
#         "price": price,
#         "deviation": 10,
#         "magic": 234000,
#         "comment": "Close trade",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }
#     result = mt5.order_send(close_request)
#     if result.retcode == mt5.TRADE_RETCODE_DONE:
#         return price  # Return exit price
#     else:
#         print(f"Failed to close trade: {result.retcode} and comment {result.comment}")
#         return None

# # # Main loop for live trading
# # balance = 1000  # Initial balance
# # while True:
# #     # Get latest price data
# #     rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 50)  # Use M1 timeframe for real-time
# #     data = pd.DataFrame(rates)
# #     data['time'] = pd.to_datetime(data['time'], unit='s')

# #     # Calculate MACD
# #     macd, macd_signal, macd_hist = get_macd(data)

# #     # Determine trade direction
# #     direction = None
# #     if macd.iloc[-1] > macd_signal.iloc[-1] and macd_hist.iloc[-1] > 0:
# #         direction = "call"
# #     elif macd.iloc[-1] < macd_signal.iloc[-1] and macd_hist.iloc[-1] < 0:
# #         direction = "put"

# #     if direction:
# #         # Execute trade
# #         order_id, entry_price = place_trade(SYMBOL, direction, TRADE_AMOUNT)
# #         if order_id is not None:
# #             print(f"Trade executed: {direction} at {entry_price}")

# #             # Wait for the trade interval to check outcome
# #             time.sleep(TRADE_INTERVAL)

# #             # Close the trade and evaluate the outcome
# #             exit_price = close_trade(order_id, direction)
# #             if exit_price is not None:
# #                 price_difference = exit_price - entry_price
# #                 result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"

# #                 # Update balance based on trade result
# #                 if result == "win":
# #                     balance += TRADE_AMOUNT * WIN_MULTIPLIER
# #                 else:
# #                     balance -= TRADE_AMOUNT * LOSE_MULTIPLIER

# #                 # Log trade result with Entry and Exit prices and Price Difference
# #                 new_row = pd.DataFrame([{
# #                     "Time": datetime.now(),
# #                     "Direction": direction,
# #                     "Entry Price": entry_price,
# #                     "Exit Price": exit_price,
# #                     "Price Difference": price_difference,
# #                     "Result": result,
# #                     "Balance": balance
# #                 }])

# #                 results = pd.concat([results, new_row], ignore_index=True)

# #                 # Save to CSV
# #                 results.to_csv(output_path, index=False)

# #                 # Print current balance
# #                 print(f"Balance after trade: ${balance:.2f}")
        
# #     # Wait a bit before the next check
# #     time.sleep(10)

# # # Shutdown MetaTrader 5 connection
# # # mt5.shutdown()


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
#         # Check account balance before trade
#         account_info = mt5.account_info()
#         if account_info is None:
#             print("Failed to retrieve account info")
#             mt5.shutdown()
#             quit()

#         # Check margin requirements
#         symbol_info = mt5.symbol_info(SYMBOL)
#         if symbol_info is None:
#             print(f"Symbol {SYMBOL} not found")
#             mt5.shutdown()
#             quit()

#         print(f"Current account balance: ${account_info.balance:.2f}")
#         required_margin = symbol_info.margin_initial * TRADE_AMOUNT
#         print(f"Required margin for trade: {required_margin}")

#         if account_info.balance < TRADE_AMOUNT:
#             print("Insufficient funds to place the trade.")
#             time.sleep(TRADE_INTERVAL)  # Wait before the next attempt
#             continue  # Skip to the next iteration if balance is too low

#         # Execute trade
#         order_id, entry_price = place_trade(SYMBOL, direction, TRADE_AMOUNT)
#         if order_id is not None:
#             print(f"Trade executed: {direction} at {entry_price}")

#             # Wait for the trade interval to check outcome
#             time.sleep(TRADE_INTERVAL)

#             # Close the trade and evaluate the outcome
#             exit_price = close_trade(order_id, direction)
#             if exit_price is not None:
#                 price_difference = exit_price - entry_price
#                 result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"

#                 # Update balance based on trade result
#                 if result == "win":
#                     balance += TRADE_AMOUNT * WIN_MULTIPLIER
#                 else:
#                     balance -= TRADE_AMOUNT * LOSE_MULTIPLIER

#                 # Log trade result with Entry and Exit prices and Price Difference
#                 new_row = pd.DataFrame([{
#                     "Time": datetime.now(),
#                     "Direction": direction,
#                     "Entry Price": entry_price,
#                     "Exit Price": exit_price,
#                     "Price Difference": price_difference,
#                     "Result": result,
#                     "Balance": balance
#                 }])

#                 results = pd.concat([results, new_row], ignore_index=True)

#                 # Save to CSV
#                 results.to_csv(output_path, index=False)

#                 # Print current balance
#                 print(f"Balance after trade: ${balance:.2f}")
        
#     # Wait a bit before the next check
#     time.sleep(10)

# # Shutdown MetaTrader 5 connection
# # mt5.shutdown()


# Keep at it

# # robust trading with Binary Options and Forex
# import MetaTrader5 as mt5
# import pandas as pd
# import time
# from datetime import datetime
# from ta.trend import MACD

# # MetaTrader 5 setup for Forex
# if not mt5.initialize():
#     print("MetaTrader5 initialization failed")
#     quit()

# # Strategy parameters
# SYMBOL = "EURUSD"
# TRADE_AMOUNT = 10.0  # Adjust this to desired trade size
# WIN_MULTIPLIER = 1.8
# LOSE_MULTIPLIER = 1.0
# TRADE_INTERVAL = 60  # Interval between trades in seconds

# # Initialize trade logging for Binary Options
# binary_output_path = "binary_trade_results5.csv"
# columns = ["Time", "Direction", "Entry Price", "Exit Price", "Price Difference", "Result", "Balance"]
# binary_results = pd.DataFrame(columns=columns)

# # Forex balance initialization (tracked within MetaTrader5)
# forex_balance = 1000  # Set your initial balance for internal tracking

# # Define strategy logic functions
# def get_macd(price_data):
#     macd_indicator = MACD(price_data['close'], window_slow=26, window_fast=12, window_sign=9)
#     return macd_indicator.macd(), macd_indicator.macd_signal(), macd_indicator.macd_diff()

# def place_trade(symbol, direction, trade_amount):
#     order_type = mt5.ORDER_TYPE_BUY if direction == "call" else mt5.ORDER_TYPE_SELL
#     price = mt5.symbol_info_tick(symbol).ask if direction == "call" else mt5.symbol_info_tick(symbol).bid
#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": trade_amount,
#         "type": order_type,
#         "price": price,
#         "deviation": 10,
#         "magic": 234000,
#         "comment": "Forex trade",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }
#     result = mt5.order_send(request)
#     if result.retcode == mt5.TRADE_RETCODE_DONE:
#         return result.order, price  # Return order ID and entry price
#     else:
#         print(f"Trade execution failed: {result.retcode} and comment: {result.comment}")
#         return None, None

# # Define functions for binary options (simulated trading)
# def record_binary_trade(direction, entry_price, result):
#     exit_price = entry_price * (1.01 if result == "win" else 0.99)
#     price_difference = exit_price - entry_price
#     new_row = pd.DataFrame([{
#         "Time": datetime.now(),
#         "Direction": direction,
#         "Entry Price": entry_price,
#         "Exit Price": exit_price,
#         "Price Difference": price_difference,
#         "Result": result,
#         "Balance": forex_balance  # Use forex_balance as a reference balance
#     }])
#     global binary_results
#     binary_results = pd.concat([binary_results, new_row], ignore_index=True)
#     binary_results.to_csv(binary_output_path, index=False)

# # Main loop for live trading
# while True:
#     # Get latest price data
#     rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 50)
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
#         # **Binary Options Trade Simulation**
#         entry_price = mt5.symbol_info_tick(SYMBOL).ask if direction == "call" else mt5.symbol_info_tick(SYMBOL).bid
#         result = "win" if (direction == "call" and macd_hist.iloc[-1] > 0) else "loss"
#         record_binary_trade(direction, entry_price, result)
#         print(f"Binary trade recorded: {direction} at {entry_price} with result: {result}")

#         # **Forex Trade Execution**
#         # Check account balance before Forex trade
#         account_info = mt5.account_info()
#         if account_info is None:
#             print("Failed to retrieve account info")
#             mt5.shutdown()
#             quit()


#         # Check margin requirements
#         symbol_info = mt5.symbol_info(SYMBOL)
#         if symbol_info is None:
#             print(f"Symbol {SYMBOL} not found")
#             mt5.shutdown()
#             quit()

#         # required_margin = symbol_info.margin_initial * TRADE_AMOUNT
#         # print(f"Required margin for Forex trade: {required_margin}")
#         # Get account leverage
#         leverage = account_info.leverage if account_info.leverage > 0 else 1  # Prevent divide by zero
#         print('leverage is ',leverage)
#         required_margin = (symbol_info.margin_initial * TRADE_AMOUNT) / leverage
#         print(f"Required margin for Forex trade: {required_margin}")

#         if account_info.balance >= TRADE_AMOUNT:
#             order_id, entry_price = place_trade(SYMBOL, direction, TRADE_AMOUNT)
#             if order_id is not None:
#                 print(f"Forex trade executed: {direction} at {entry_price}")
#                 # Close trade after interval (for demo purposes, consider trade duration adjustments)
#                 time.sleep(TRADE_INTERVAL)
#                 exit_price = close_trade(order_id, direction)
#                 if exit_price is not None:
#                     price_difference = exit_price - entry_price
#                     result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"
#                     forex_balance += TRADE_AMOUNT * WIN_MULTIPLIER if result == "win" else -TRADE_AMOUNT * LOSE_MULTIPLIER
#                     print(f"Forex Balance after trade: ${forex_balance:.2f}")

#     time.sleep(10)

# mt5.shutdown()




# # robust trading with Binary Options and Forex
# import MetaTrader5 as mt5
# import pandas as pd
# import time
# from datetime import datetime
# from ta.trend import MACD

# # MetaTrader 5 setup for Forex
# if not mt5.initialize():
#     print("MetaTrader5 initialization failed")
#     quit()

# # Strategy parameters
# SYMBOL = "EURUSD"
# TRADE_AMOUNT = 10.0  # Adjust this to desired trade size
# WIN_MULTIPLIER = 1.8
# LOSE_MULTIPLIER = 1.0
# TRADE_INTERVAL = 60  # Interval between trades in seconds

# # Initialize trade logging for Binary Options
# binary_output_path = "binary_trade_results6.csv"
# columns = ["Time", "Direction", "Entry Price", "Exit Price", "Price Difference", "Result", "Balance"]
# binary_results = pd.DataFrame(columns=columns)

# # Forex balance initialization (tracked within MetaTrader5)
# forex_balance = 1000  # Set your initial balance for internal tracking

# # Define strategy logic functions
# def get_macd(price_data):
#     macd_indicator = MACD(price_data['close'], window_slow=26, window_fast=12, window_sign=9)
#     return macd_indicator.macd(), macd_indicator.macd_signal(), macd_indicator.macd_diff()

# def place_trade(symbol, direction, trade_amount):
#     order_type = mt5.ORDER_TYPE_BUY if direction == "call" else mt5.ORDER_TYPE_SELL
#     price = mt5.symbol_info_tick(symbol).ask if direction == "call" else mt5.symbol_info_tick(symbol).bid
#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": symbol,
#         "volume": trade_amount,
#         "type": order_type,
#         "price": price,
#         "deviation": 10,
#         "magic": 234000,
#         "comment": "Forex trade",
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }
#     result = mt5.order_send(request)
#     if result.retcode == mt5.TRADE_RETCODE_DONE:
#         return result.order, price  # Return order ID and entry price
#     else:
#         print(f"Trade execution failed: {result.retcode} and comment: {result.comment}")
#         return None, None

# # Define functions for binary options (simulated trading)
# def record_binary_trade(direction, entry_price, result):
#     exit_price = entry_price * (1.01 if result == "win" else 0.99)
#     price_difference = exit_price - entry_price
#     new_row = pd.DataFrame([{
#         "Time": datetime.now(),
#         "Direction": direction,
#         "Entry Price": entry_price,
#         "Exit Price": exit_price,
#         "Price Difference": price_difference,
#         "Result": result,
#         "Balance": forex_balance  # Use forex_balance as a reference balance
#     }])
#     global binary_results
#     binary_results = pd.concat([binary_results, new_row], ignore_index=True)
#     binary_results.to_csv(binary_output_path, index=False)

# # Function to close Forex trades
# def close_trade(order_id, direction):
#     order_type = mt5.ORDER_TYPE_SELL if direction == "call" else mt5.ORDER_TYPE_BUY  # Opposite action to close
#     price = mt5.symbol_info_tick(SYMBOL).bid if direction == "call" else mt5.symbol_info_tick(SYMBOL).ask
#     request = {
#         "action": mt5.TRADE_ACTION_DEAL,
#         "symbol": SYMBOL,
#         "volume": TRADE_AMOUNT,
#         "type": order_type,
#         "price": price,
#         "deviation": 10,
#         "magic": 234000,
#         "comment": "Forex trade close",
#         "position": order_id,
#         "type_time": mt5.ORDER_TIME_GTC,
#         "type_filling": mt5.ORDER_FILLING_IOC,
#     }
#     result = mt5.order_send(request)
#     if result.retcode == mt5.TRADE_RETCODE_DONE:
#         return price  # Return exit price
#     else:
#         print(f"Failed to close trade: {result.retcode}")
#         return None

# # Main loop for live trading
# while True:
#     # Get latest price data
#     rates = mt5.copy_rates_from_pos(SYMBOL, mt5.TIMEFRAME_M1, 0, 50)
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
#         # **Binary Options Trade Simulation**
#         entry_price = mt5.symbol_info_tick(SYMBOL).ask if direction == "call" else mt5.symbol_info_tick(SYMBOL).bid
#         result = "win" if (direction == "call" and macd_hist.iloc[-1] > 0) else "loss"
#         record_binary_trade(direction, entry_price, result)
#         print(f"Binary trade recorded: {direction} at {entry_price} with result: {result}")

#         # **Forex Trade Execution**
#         # Check account balance before Forex trade
#         account_info = mt5.account_info()
#         if account_info is None:
#             print("Failed to retrieve account info")
#             mt5.shutdown()
#             quit()

#         # Check margin requirements
#         symbol_info = mt5.symbol_info(SYMBOL)
#         if symbol_info is None:
#             print(f"Symbol {SYMBOL} not found")
#             mt5.shutdown()
#             quit()

#         leverage = account_info.leverage if account_info.leverage > 0 else 1  # Prevent divide by zero
#         print('leverage is ', leverage)
#         required_margin = (symbol_info.margin_initial * TRADE_AMOUNT) / leverage
#         print(f"Required margin for Forex trade: {required_margin}")

#         if account_info.balance >= required_margin:
#             order_id, entry_price = place_trade(SYMBOL, direction, TRADE_AMOUNT)
#             if order_id is not None:
#                 print(f"Forex trade executed: {direction} at {entry_price}")
#                 # Close trade after interval (for demo purposes, consider trade duration adjustments)
#                 time.sleep(TRADE_INTERVAL)
#                 exit_price = close_trade(order_id, direction)
#                 if exit_price is not None:
#                     price_difference = exit_price - entry_price
#                     result = "win" if (direction == "call" and exit_price > entry_price) or (direction == "put" and exit_price < entry_price) else "loss"
#                     forex_balance += TRADE_AMOUNT * WIN_MULTIPLIER if result == "win" else -TRADE_AMOUNT * LOSE_MULTIPLIER
#                     print(f"Forex Balance after trade: ${forex_balance:.2f}")

#     time.sleep(10)

# mt5.shutdown()


# improved
# Robust trading with Binary Options and Forex
import MetaTrader5 as mt5
import pandas as pd
import time
from datetime import datetime
from ta.trend import MACD

# Initialize MetaTrader 5
if not mt5.initialize():
    print("MetaTrader5 initialization failed")
    quit()

# Strategy parameters
SYMBOLS = ["EURUSD", "GBPUSD", "ETHUSD"]  # Add any additional symbols you want to trade
TRADE_AMOUNT = 0.1  # Trade size, adjust as necessary
WIN_MULTIPLIER = 1.8
LOSE_MULTIPLIER = 1.0
TRADE_INTERVAL = 60  # Interval between trades in seconds

# Additional trade parameters
TAKE_PROFIT_MULTIPLIER = 1.01  # 1% profit target
STOP_LOSS_MULTIPLIER = 0.99      # 1% loss limit

# Initialize trade logging for Binary Options
binary_output_path = "binary_trade_results7.csv"
columns = ["Time", "Direction", "Entry Price", "Exit Price", "Price Difference", "Result", "Balance"]
binary_results = pd.DataFrame(columns=columns)

# Forex balance initialization (tracked within MetaTrader5)
forex_balance = 1000  # Set your initial balance for internal tracking

# Define strategy logic functions
def get_macd(price_data):
    macd_indicator = MACD(price_data['close'], window_slow=26, window_fast=12, window_sign=9)
    return macd_indicator.macd(), macd_indicator.macd_signal(), macd_indicator.macd_diff()

def place_trade(symbol, direction, trade_amount):
    order_type = mt5.ORDER_TYPE_BUY if direction == "buy" else mt5.ORDER_TYPE_SELL
    price = mt5.symbol_info_tick(symbol).ask if direction == "buy" else mt5.symbol_info_tick(symbol).bid
    take_profit = price * TAKE_PROFIT_MULTIPLIER if direction == "buy" else price * (2 - TAKE_PROFIT_MULTIPLIER)
    stop_loss = price * STOP_LOSS_MULTIPLIER if direction == "buy" else price * (2 - STOP_LOSS_MULTIPLIER)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": trade_amount,
        "type": order_type,
        "price": price,
        "deviation": 10,
        "magic": 234000,
        "comment": "Strategy Trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
        "tp": take_profit,  # Set take profit
        "sl": stop_loss,    # Set stop loss
    }
    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"Trade executed: {direction} {trade_amount} lots at {price} for {symbol} (Order ID: {result.order})")
        return result.order, price  # Return order ID and entry price
    else:
        print(f"Trade execution failed: {result.retcode} and comment: {result.comment}")
        return None, None

# Define functions for binary options (simulated trading)
def record_binary_trade(direction, entry_price, result):
    exit_price = entry_price * (1.01 if result == "win" else 0.99)
    price_difference = exit_price - entry_price
    new_row = pd.DataFrame([{
        "Time": datetime.now(),
        "Direction": direction,
        "Entry Price": entry_price,
        "Exit Price": exit_price,
        "Price Difference": price_difference,
        "Result": result,
        "Balance": forex_balance  # Use forex_balance as a reference balance
    }])
    global binary_results
    binary_results = pd.concat([binary_results, new_row], ignore_index=True)
    binary_results.to_csv(binary_output_path, index=False)

# Main loop for live trading
while True:
    for symbol in SYMBOLS:
        # Get latest price data
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 50)
        data = pd.DataFrame(rates)
        data['time'] = pd.to_datetime(data['time'], unit='s')

        # Calculate MACD
        macd, macd_signal, macd_hist = get_macd(data)

        # Determine trade direction
        direction = None
        if macd.iloc[-1] > macd_signal.iloc[-1] and macd_hist.iloc[-1] > 0:
            direction = "buy"
        elif macd.iloc[-1] < macd_signal.iloc[-1] and macd_hist.iloc[-1] < 0:
            direction = "sell"

        if direction:
            # **Binary Options Trade Simulation**
            entry_price = mt5.symbol_info_tick(symbol).ask if direction == "buy" else mt5.symbol_info_tick(symbol).bid
            result = "win" if (direction == "buy" and macd_hist.iloc[-1] > 0) else "loss"
            record_binary_trade(direction, entry_price, result)
            print(f"Binary trade recorded: {direction} at {entry_price} with result: {result}")

            # **Forex Trade Execution**
            # Check account balance before Forex trade
            account_info = mt5.account_info()
            if account_info is None:
                print("Failed to retrieve account info")
                mt5.shutdown()
                quit()

            # Check margin requirements
            symbol_info = mt5.symbol_info(symbol)
            if symbol_info is None:
                print(f"Symbol {symbol} not found")
                mt5.shutdown()
                quit()

            # Get account leverage
            leverage = account_info.leverage if account_info.leverage > 0 else 1  # Prevent divide by zero
            print('Leverage is ', leverage)
            required_margin = (symbol_info.margin_initial * TRADE_AMOUNT) / leverage
            print(f"Required margin for Forex trade: {required_margin}")

            if account_info.balance >= required_margin:
                order_id, entry_price = place_trade(symbol, direction, TRADE_AMOUNT)
                if order_id is not None:
                    print(f"Forex trade executed: {direction} at {entry_price}")
                    # Close trade after interval (for demo purposes, consider trade duration adjustments)
                    time.sleep(TRADE_INTERVAL)
                    # Note: Closing logic not implemented, this should be handled based on your strategy

                    # Update balance (this is just a simulation)
                    forex_balance += TRADE_AMOUNT * WIN_MULTIPLIER if result == "win" else -TRADE_AMOUNT * LOSE_MULTIPLIER
                    print(f"Forex Balance after trade: ${forex_balance:.2f}")

    time.sleep(10)

mt5.shutdown()
