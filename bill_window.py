# <<<<<<< HEAD dd
def bill(typ=0):
    temp = {}
    temp_lt = []
    while True:
        item_no = int(input('Item_no: '))
        quantity = int(input('quantity'))
        temp_lt.append((item_no, quantity))
        temp[item_no] = quantity
        print("do you want to enter more items y/n?".upper())
        uio = input("-->")
        if uio.upper() == "N":
            break
    # return temp
    if typ:
        return temp_lt
    elif not typ:
        return temp
    else:
        return

