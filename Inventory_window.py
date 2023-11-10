from database import *

tab = 'INVENTORY'

print('INVENTORY')
for i in view_table(tab):
    for h in i:
        print(h,end=" ")
    print("")
