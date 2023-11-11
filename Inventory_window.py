from function_set import *
from database import *

tab = 'INVENTORY'

t = align_records_with_head(view_table(tab), tab)

for i in range(0, len(t)):
    for j in t:
        print(j[i], end='| ')
    print()



