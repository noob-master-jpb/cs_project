from combine import *

vtrl = 0

while not vtrl:
    print("1. NEW BILL\n"
          "2. INVENTORY\n"
          "3. SALES HISTORY\n"
          "4. EXIT")

    win = int(input("--->"))
    if win == 1:
        print(1)
    elif win == 2:
        take_control("INVENTORY")
    elif win == 3:
        take_control("SALES")
    elif win == 4:
        vtrl = 1
