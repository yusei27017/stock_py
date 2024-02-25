import pandas as pd
import requests
import json

# print("hello world")
if __name__ == "__main__":
    print("start")
    sess = requests.session()
    res = sess.get("https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20240223&type=ALL&response=json")
    res_json = json.loads(res.text)
    data_tbl = res_json['tables']
    tbl_all_data = data_tbl[8]['data']
    df = pd.DataFrame(tbl_all_data)
    df.astype(str)
    print(df)
    # print(tbl_all_data[:100])