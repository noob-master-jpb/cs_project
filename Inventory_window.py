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
at = int(input("---> "))
if at == 1:
    print("1. by NAME")
    print("2. by COST PRICE")
    print("3. by SELL PRICE")
    print("4. by DATE ADDED")
    print("5. by EXPIRY DATE")


