m =int(input("Введите количество метров:"))
nnumber = input("1 -Ответ в милях, 2 -Ответ в дюймах, 3 -Ответ в ярдах  ")

ml = m * 0.00062
dm = m * 39.37
yr = m * 1.09

if nnumber == '1':
    print("Ответ в милях:", ml)
elif  nnumber == '2':
    print("Ответ в дюймах:", dm)
elif  nnumber == '3':    
    print("Ответ в ярдах:", yr)

