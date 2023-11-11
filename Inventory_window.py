from function_set import *
from database import *

tab = 'INVENTORY'
print("ALL RECORDS")
def show_all_inventory(rec = view_table(tab),table = tab):
    t = align_records_with_head(rec, table)
    for i in range(0, len(t)):
        for j in t:
            print(j[i], end='| ')
        print()
show_all_inventory()
print("1. To USE FILTER")
print("2. To USE SORTING")
at = int(input("--> "))
if at == 1:
    print("1. by COST PRICE")
    print("2. by SELL PRICE")
    print("3. by DATE ADDED")
    print("4. by EXPIRY DATE")
    ap = int(input("--> "))
    if ap == 1:
        print("PUT THE RANGE OF COST PRICE")
        up = int(input("FROM--> "))
        down = int(input("TO--> "))
        print(up,down)

    elif ap == 2:
        print("PUT THE RANGE OF SELL PRICE")
        up = int(input("FROM--> "))
        down = int(input("TO--> "))
        print(up, down)
    elif ap == 3:
        print("PUT THE RANGE OF DATE ADDED")
        up = int(input("FROM--> "))
        down = int(input("TO--> "))
        print(up, down)
    elif ap == 3:
        print("PUT THE RANGE OF EXPIRY DATE")
        up = int(input("FROM--> "))
        down = int(input("TO--> "))
        print(up, down)

