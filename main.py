from binance.client import Client

api_key = 'al3IIENiD8Z0udKHdpTGHww5wQGGK6i1pNbqWuumsGzLPboRVBgc9PvOH2CxcAqp'
secret_key = 'E0srxhUEQJGBw6r6jqWqEvba3jcgPnBOnlqRP94M2PfMuSjAkKkalVqW0oSrrOYA'

client = Client(
    api_key,
    secret_key,
    testnet=True
)

tickers = client.get_all_tickers()
print(tickers[0]['symbol'])


#for ticker in tickers:
   # print(ticker['symbol'])