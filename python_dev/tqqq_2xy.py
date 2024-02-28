import yfinance as yf
import pandas as pd

def get_qttt_data(start_date = None, end_dat = None):
    tqqq = yf.Ticker('TQQQ')
    tqqq_data = tqqq.history(period="4y", interval="1d")
    df = pd.DataFrame(tqqq_data)
    return df

def backtesting_2xy(cost, df):
    total_cost, stock, profit = cost, cost, 0
    prev_price = df['Close'].iloc[0]
    for close in df['Close'][1:]:

        volatility = close / prev_price
        if volatility > 1:
            change = stock * (volatility - 1)
            stock -= change
            profit += change
        else:
            change = stock * (1 - volatility)
            stock += change
            profit -= change
        prev_price = close 
        print(f"profit:{profit} stock:{stock} res:{round(profit+stock)}")

    return stock, profit

if __name__ == "__main__":
    df = get_qttt_data()
    stock, profit = backtesting_2xy(1000, df)
    # print()