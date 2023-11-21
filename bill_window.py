def bill():
    temp = {}
    while True:
        item_no = int(input('Item_no: '))
        quantity = int(input('quantity'))
        temp[item_no] = quantity
        print("do you want to enter more items y/n?".upper())
        uio = input("-->")
        if uio.upper() == "N":
            break
    return temp