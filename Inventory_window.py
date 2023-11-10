from function_set import *
from database import *

tab = 'INVENTORY'

# print('INVENTORY')
# for i in view_table(tab):
#     a = align_field(i, )
#     for h in a:
#         print(align_field(h, tab), end=" ")
#     print("")

# for j in range(att_no(tab)):
#     for i in align_field_head(j, tab):
#         print(i, end=' |')
#         print()
t = []
for j in range(att_no(tab)):
    t.append(align_field_head(j, tab))

field_to_row(t)
# for i in ret_header(tab):
#     print(i)
#
#
#
# for i in align_row_head(view_table(tab),tab):
#     print("|",end=' ')
#     for j in i:
#         print(j, end= ' | ')
#     print('')
