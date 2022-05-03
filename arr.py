arr = [{'symbol': 'BNBBUSD', 'price': '153.63000000'}, {'symbol': 'BTCBUSD', 'price': '37800.00000000'},
       {'symbol': 'ETHBUSD', 'price': '2879.24000000'}, {'symbol': 'LTCBUSD', 'price': '100.10000000'}]


def destructor_json(argument):
    index = list()
    content = list()

    for element in argument:
        index.append(element['symbol'])
        content.append(element['price'])
    return index, content


def create_list(argument, function):
    keys, values = function(argument)
    return dict(zip(keys, values))


print(create_list(arr, destructor_json))
