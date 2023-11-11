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
