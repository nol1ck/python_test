from Ticker import Ticker
from table.table import Table as table

arr = [{'symbol': 'BNBBUSD', 'price': '153.63000000'}, {'symbol': 'BTCBUSD', 'price': '37800.00000000'},
       {'symbol': 'ETHBUSD', 'price': '2879.24000000'}, {'symbol': 'LTCBUSD', 'price': '100.10000000'}]


ticker = Ticker(arr)

print(ticker.create_list())

function_print = table('work')
function_print.work()


