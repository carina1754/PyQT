import pyupbit
price = pyupbit.get_current_price("KRW-MOC")
print(price)
df = pyupbit.get_ohlcv("KRW-MOC")
print(df)
df1 = pyupbit.get_ohlcv("KRW-MOC", interval="minute")
print(df1)

ac = "FP1tlQxBE4eeY1PKl3C0iHmGCBvxgXayRHeQxvJf"
sc = "GfJqrFN1uiMdj3p222Xjxom7tZtyHn0ZH5lNSfT0"

upbit = (pyupbit.Upbit(ac, sc)).get_balances()
print(upbit)
