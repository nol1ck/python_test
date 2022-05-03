first_List = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

second_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


result = list(filter(lambda elem: elem in second_List, first_List))


