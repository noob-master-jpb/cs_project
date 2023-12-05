from random import *
# <<<<<<< HEAD
from database import *
from datetime import *
from function_set import *


def bill(typ=0):
    temp = {}
    temp_lt = []
    while True:
        item_no = int(input('Item_no: '))
        quantity = int(input('Quantity: '))
        temp_lt.append((item_no, quantity))
        temp[item_no] = quantity
        print("do you want to enter more items y/n?".upper())
        uio = input("-->")
        if uio.upper() != "Y":
            break

    # return temp
    if typ:
        return temp_lt
    elif not typ:
        return temp
    else:
        return



def gen_bill():
    prev_bill_no = [i[0] for i in view_table("sales")]
    bi = bill()
    all_dat = out_rec_dict(bi)
    actual_rec = []
    current_bill_no = max(prev_bill_no) + 1
    for i in all_dat:
        ttl = (current_bill_no, date.today(), i[0], i[1],bi[i[0]], i[5],  "10",
               int((int(bi[i[0]]) * int(i[5])) + (((int(bi[i[0]]) * int(i[5])) / 100) * 10) // 1))
        actual_rec.append(ttl)
    display_record = align_records_with_head(actual_rec, "sales")[2:]
    print(f"BILL NO : {current_bill_no} ")
    print(f"Date : {date.today()}")
    for i in field_to_row(display_record):
        for j in i:
            print(j, end='| ')
        print()
    print(f"TOTAL AMOUNT = Rs {sum([int(i) for i in display_record[-1][1:]])}")
    input_data("sales",actual_rec)
