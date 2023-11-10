from function_set import *
from database import *

tab = 'INVENTORY'

# print('INVENTORY')
# for i in view_table(tab):
#     a = align_field(i, )
#     for h in a:
#         print(align_field(h, tab), end=" ")
#     print("")
#
for i in align_row(view_table(tab),tab):
    print("|",end=' ')
    for j in i:
        print(j, end= ' | ')
    print('')