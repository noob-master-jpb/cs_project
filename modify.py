from database import *
from function_set import *

def update_inventory():
    print("ENTER THE ITEM NO OF THE RECORD YOU WANT TO UPDATE")
    mod_id = input("-->")
    control.execute(f"select * from inventory where item_no = {mod_id}")
    id_rec = control.fetchall()
    print("Present Record")

    for j in field_to_row(align_records_with_head(id_rec,"inventory")):
        for k in j:
            print(k, end="| ")
        print()

    print("SELECT WHAT YOU WANT TO CHANGE")

    for i in enumerate(table_structure("inventory")[1:]):
        print(f"{i[0]+1}. {i[1][0]}")
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
    for j in field_to_row(align_records_with_head(id_rec,"inventory")):
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


