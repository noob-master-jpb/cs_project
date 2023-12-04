from combine import *
from bill_window import *
from modify import *

vtrl = 0

while not vtrl:
    print("1. NEW BILL\n"
          "2. INVENTORY\n"
          "3. UPDATE INVENTORY\n"
          "4. SALES HISTORY\n"
          "5. EXIT")

    win = int(input("--->"))
    if win == 1:
        gen_bill()
    elif win == 2:
        take_control("INVENTORY")
    elif win == 3:
        print("1.MODIFY RECORD\n"
              "2.DELETE RECORD")
        we = int(input("-->"))
        if we == 1:
            update_inventory()
        elif we == 2:
            delete_inventory()
    elif win == 4:
        take_control("SALES")
    elif win == 5:
        vtrl = 1
