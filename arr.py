arr = [{'symbol': 'BNBBUSD', 'price': '153.63000000'}, {'symbol': 'BTCBUSD', 'price': '37800.00000000'},
       {'symbol': 'ETHBUSD', 'price': '2879.24000000'}, {'symbol': 'LTCBUSD', 'price': '100.10000000'}]

keys = list()

for item in arr:
    keys.append(item['symbol'])

values = list()

for item in arr:
    values.append(item['price'])

new_arr = dict(zip(keys, values))
print(new_arr['BNBBUSD'])








