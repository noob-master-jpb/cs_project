from database import *
from function_set import *
from datetime import *


def update_inventory():
    print("ENTER THE ITEM NO OF THE RECORD YOU WANT TO UPDATE")
    mod_id = input("-->")
    control.execute(f"select * from inventory where item_no = {mod_id}")
    id_rec = control.fetchall()
    print("Present Record")

    for j in field_to_row(align_records_with_head(id_rec, "inventory")):
        for k in j:
            print(k, end="| ")
        print()

    print("SELECT WHAT YOU WANT TO CHANGE")

    for i in enumerate(table_structure("inventory")[1:]):
        print(f"{i[0] + 1}. {i[1][0]}")
    prop_id = input("-->")
    hed = [i[0] for i in table_structure("inventory")][int(prop_id)]
    print(hed)
    print("ENTER THE NEW VALUE")
    new_dat = input("-->")

    print(control.execute(f"update inventory set {hed}='{new_dat}' where item_no = {mod_id};"))
    connection.commit()


def delete_inventory():
    print("ENTER THE ITEM NO OF THE RECORD YOU WANT TO DELETE")
    mod_id = input("-->")
    control.execute(f"select * from inventory where item_no = {mod_id}")
    id_rec = control.fetchall()
    print("Record")
    for j in field_to_row(align_records_with_head(id_rec, "inventory")):
        for k in j:
            print(k, end="| ")
        print()
    print("ARE YOU SURE YOU WANT TO DELETE IT? Y/N")
    des = input()
    if des.upper() == 'Y':
        control.execute(f"DELETE FROM INVENTORY WHERE ITEM_NO = '{mod_id}' ")
    else:
        return
    connection.commit()


def add_item_inv():
    gft = True
    all_item = []
    while gft:
        item_no = int(input("ENTER ITEM_NO: "))
        item_name = input("ENTER ITEM NAME: ")
        batch_no = int(input("ENTER BATCH NO: "))
        cost_p = int(input("ENTER COST PRICE: "))
        sell_p = int(input("ENTER SELL PRICE: "))
        quantity = int(input("ENTER QUANTITY: "))
        date_added = date.today()
        exp_date = input("ENTER EXPIRY DATE: ")
        all_item.append((item_no, item_name, batch_no, cost_p, sell_p, quantity, date_added, exp_date))
        print("DO YOU WANT TO ADD MORE ITEMS? Y/N")
        sty = input()
        if sty.upper() != "Y":
            break
    input_data("inventory", all_item)



