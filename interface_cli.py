from combine import  *

print("1. NEW BILL\n"
      "2. INVENTORY\n"
      "3. SALES HISTORY")
win = int(input("--->"))

if win == 1:
    print(1)
elif win == 2:
    take_control("INVENTORY")
elif win == 3:
    take_control("SALES")
