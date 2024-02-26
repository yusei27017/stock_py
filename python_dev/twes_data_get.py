import pandas as pd
import requests
import json
from datetime import date

sess = requests.session()

def crawl_twse_data(crawl_date):
    twse_url = f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={crawl_date}&type=ALL&response=json"
    res = sess.get(twse_url)
    res_json = json.loads(res.text)
    data_tbl = res_json['tables']
    tbl_all_data = data_tbl[8]['data']
    df = pd.DataFrame(tbl_all_data)
    df.astype(str)
    df = df.apply(lambda s: s.str.replace(',', ''))
    df['date'] = pd.to_datetime(crawl_date)
    # 將「證券代號」的欄位改名成「stock_id」
    df = df.rename(columns={0:'stock_id'})
    # 將 「stock_id」與「date」設定成index 
    df = df.set_index(['stock_id', 'date'])
    # 將所有的表格元素都轉換成數字，error='coerce'的意思是說，假如無法轉成數字，則用 NaN 取代
    df = df.apply(lambda s:pd.to_numeric(s, errors='coerce'))    
    # 刪除不必要的欄位
    df = df[df.columns[df.isnull().all() == False]]
    return df

if __name__ == "__main__":
    print("start")
    # today = date.today()
    # formatted_date = today.strftime('%Y%m%d')
    df = crawl_twse_data("20240223")
    print(df.head())