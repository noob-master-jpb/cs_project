from datetime import *
from pymysql import *
import pymysql

def count_row_len(ind, table):
    all = view_table(table)
    lt = 0
    for i in all:
        i = str(i[ind])
        if len(i) > lt:
            lt = len(i)
    return lt


def ret_header(table):
    tem = []
    for c in table_structure(table):
        tem.append(c[0])
    return tem


def field_to_row(lis):
    temp = []
    for j in range(0, len(lis[0])):
        t = []
        for i in lis:
            t.append(i[j])
        temp.append(t)
    return temp


def align_records_with_head(records, table):
    t = field_to_row(records)
    heads = ret_header(table)
    for ie in t:
        i = [heads[t.index(ie)]] + list(ie)
        t[t.index(ie)] = i

    for i in t:
        for j in i:
            i[i.index(j)] = str(j)
        max_len = len(max(i, key=len))
        for k in i:
            if len(k) < max_len:
                i[i.index(k)] = " " * (max_len - len(k)) + k
    return t


def sort_field_seq(id, table, srs=None):
    if not srs:
        sd = view_table(table)
    else:
        sd = list(srs)
    sk = [i[id] for i in sd]
    sk = list(enumerate(sk))
    ct = 0
    for g in range(len(sk)):
        tk = list(sk)
        for i in range(g % 2, len(sk) - (g % 2), 2):
            try:
                if sk[i][1] > sk[i + 1][1]:
                    sk[i], sk[i + 1] = sk[i + 1], sk[i]
            except IndexError:
                pass
        if sk == tk:
            ct += 1
            # print(ct)!
        # print(sk)
        if ct >= 2:
            break
    temp = []
    for go in sk:
        temp.append(go[0])
    return temp


connection = Connect(host="localhost",
                     user='root',
                     password="root",
                     db="project_main")
control = connection.cursor()

sales_table = """(
        BILL_NO INT NOT NULL PRIMARY KEY,
        BILL_DATE DATE,
        ITEM_NO INT,
        ITEM_NAME CHAR(20),
        QUANTITY INT,
        PRICE INT,
        TAX INT,
        TOTAL INT
        );"""

inventory_table = """(
        ITEM_NO INT NOT NULL PRIMARY KEY,
        ITEM_NAME CHAR(20),
        BATCH_NO INT,
        COST_PRICE INT,
        SELL_PRICE INT,
        QUANTITY INT,
        DATE_ADDED DATE,
        EXPIRY DATE
        );"""


def att_no(table):
    return control.execute("""describe """ + table)


def view_table(table=''):
    if table == '':
        print("NO TABLE NAME GIVEN")
    control.execute(("""SELECT * FROM """ + table + """;"""))
    return control.fetchall()


def table_structure(table=''):
    if table == '':
        print("NO TABLE INPUT")
        return
    control.execute(f'describe {table}')
    return control.fetchall()


def input_data(table, lis=[]):
    if not lis:
        print("NO INPUT")
        return
    field_ctrl = '%s,' * att_no(table)
    try:
        control.executemany("""INSERT INTO """ + table + """ VALUES(""" + field_ctrl[:-1] + """)""", lis)
    except pymysql.err.DataError:
        print("INVALID INPUT")
        return None

    connection.commit()


def reset_table(table=''):
    ctrl = ''
    if table == '':
        print("NO TABLE NAME GIVEN")
    elif table.upper() == 'SALES':
        ctrl = sales_table
    elif table.upper() == 'INVENTORY':
        ctrl = inventory_table
    else:
        print("TABLE DES NOT EXIST")
        return
    control.execute("""DROP TABLE IF EXISTS """ + table + """;""")
    control.execute("""CREATE TABLE """ + table + ctrl)


def out_rec_dict(a=None):
    if a is None:
        a = {}
    k = []
    for i in a.keys():
        control.execute(f"select * from inventory where item_no = {i};")
        k.append(control.fetchall()[0])
    return k


# def out_fields_tab(feild=None, tab=None):
#     if (not feild) or (not tab):
#         return
#     control.execute(f"select {feild} from {tab}")
#     return control.fetchall()


def show_table(rec, table):
    t = align_records_with_head(rec, table)
    sort_sq = range(0, len(rec) + 1)
    for i in sort_sq:
        for j in t:
            print(j[i], end='| ')
        print()
    return t


def filter(tab):
    if not tab:
        print("table name is mandatory".upper())
        return
    if tab.upper() == "INVENTORY":
        ls = ['COST_PRICE', "SELL_PRICE", "QUANTITY", "DATE_ADDED", "EXPIRY"]
        v = -2
    elif tab.upper() == "SALES":
        ls = ["QUANTITY", "PRICE", "TOTAL", 'BILL_DATE']
        v = -1
    else:
        print("table not included in function".upper())
        return
    for i in enumerate(ls):
        print(f"{i[0] + 1}. by {i[1].replace('_', ' ')}")
    try:
        ap = int(input("--> "))
    except ValueError:
        print("INVALID INPUT")
        return
    try:
        print(f"PUT THE RANGE OF {ls[ap - 1].replace('_', ' ')}")
    except IndexError:
        print("INVALID INPUT")
        return
    up = input("FROM--> ")
    down = input("TO--> ")

    if ls[ap] not in ls[v:]:
        try:
            up = int(up)
            down = int(down)
        except ValueError:
            print("INVALID INPUT")
            return
    else:
        up = "'" + up + "'"
        down = "'" + down + "'"
    # print(f"SELECT * FROM {tab} WHERE {ls[ap-1]} BETWEEN {up} AND {down};".upper())
    num_rec = control.execute(f"SELECT * FROM {tab} WHERE {ls[ap - 1]} BETWEEN {up} AND {down};".upper())
    print(num_rec, "RECORDS FOUND")
    if num_rec == 0:
        return None
    filt_data = control.fetchall()
    show_table(filt_data, tab)
    return filt_data


def take_control(tab):
    if tab.upper() == "INVENTORY":
        inv = 1
    else:
        inv = 0
    header = ret_header(tab)
    # all_rec = view_table(tab)
    # tt = show_table(view_table(tab), tab)
    ctrl = 0
    print("ALL RECORDS")
    while not ctrl:
        lo = ["To USE FILTER", "To USE SORTING", "ADD ITEMS", "MODIFY ITEM", "DELETE ITEM", "To CLOSE"]
        if inv:
            for i in enumerate(lo):
                print(f"{i[0] + 1}. {i[1]}")
        else:
            lo = ["To USE FILTER", "To USE SORTING", "To CLOSE"]
            for i in enumerate(lo):
                print(f"{i[0] + 1}. {i[1]}")
        # print("1. To USE FILTER")
        # print("2. To USE SORTING")
        # print("3. To CLOSE")
        try:
            at = int(input("--> "))
        except ValueError:
            print("INVALID INPUT")
            continue
        if at == 1:
            temp_data = filter(tab)
            if temp_data == None:
                continue
            print("DO YOU WANT TO SORT THIS TABLE? y/n")
            sr = input("-->")
            if sr.upper() == 'Y':
                for i in enumerate(header):
                    print(f"{i[0] + 1}. by {i[1].replace('_', ' ')}")
                try:
                    srt = int(input("-->"))
                except ValueError:
                    print("INVALID INPUT")
                    continue
                print("1. ascending".upper())
                print("2. Descending".upper())
                srt_type = int(input("-->"))
                sort_seq = sort_field_seq(srt - 1, tab, temp_data)
                if srt_type == 2:
                    sort_seq.reverse()
                elif srt_type == 1:
                    print()
                else:
                    print("invalid input".upper())
                show_table([temp_data[i] for i in sort_seq], tab)
        elif at == 2:
            for i in enumerate(header):
                print(f"{i[0] + 1}. by {i[1].replace('_', ' ')}"),
            try:
                srt = int(input("-->"))
            except ValueError:
                print("INVALID INPUT")
                continue
            print("1. ascending".upper())
            print("2. Descending".upper())
            try:
                srt_type = int(input("-->"))
            except ValueError:
                print("INVALID INPUT")
                continue
            sort_seq = sort_field_seq(srt - 1, tab)
            if srt_type == 2:
                sort_seq.reverse()
            elif srt_type == 1:
                print()
            else:
                print("invalid input".upper())
            show_table([view_table(tab)[i] for i in sort_seq], tab)
        elif at == 3:
            if not inv:
                ctrl = 1
            else:
                zt = 1
                print("input the items and when you are done input 'exit' to quit".upper())
                temp = []
                ctz = 0
                while zt:
                    print(f"FOR ITEM {ctz + 1}")
                    tmp = []
                    for i in header:
                        if i == "DATE_ADDED":
                            adit = date.today()
                            tmp.append(adit)
                            continue
                        print(i.replace("_"," "))
                        adit = input("-->")
                        if adit.upper() == 'exit'.upper():
                            zt = 0
                            break
                        tmp.append(adit)
                    if (tmp) and (len(tmp) == 8):
                        temp.append(tuple(tmp))
                    elif not (len(tmp) == 8):
                        print("not enough for the item".upper())
                    ctz += 1
                input_data(tab, temp)
        elif at == 4:
            if not inv:
                ctrl = 1
            else:
                print("ENTER THE ITEM NO OF THE RECORD YOU WANT TO UPDATE")
                try:
                    mod_id = int(input("-->"))
                except ValueError:
                    print("invalid input".upper())
                    continue
                except IndexError:
                    print("WRONG ITEM NO")
                    continue
                control.execute(f"select * from inventory where item_no = {mod_id}")
                id_rec = control.fetchall()
                print("Present Record")
                if id_rec == ():
                    print("ITEM NOT FOUND")
                    continue
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
        elif at == 5:
            if not inv:
                ctrl = 1
            else:
                print("ENTER THE ITEM NO OF THE RECORD YOU WANT TO DELETE")
                try:
                    mod_id = int(input("-->"))
                except ValueError:
                    print("INVALID INPUT")
                    continue
                control.execute(f"select * from inventory where item_no = {mod_id}")
                id_rec = control.fetchall()
                if id_rec == ():
                    print("RECORD NOT FOUND")
                    continue
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
        elif at == 6:
            ctrl = 1


def bill(typ=0):
    temp = {}
    temp_lt = []
    while True:
        try:
            item_no = int(input('Item_no: '))
        except ValueError:
            print("Invalid input try again")
            continue
        try:
            quantity = int(input('Quantity: '))
        except ValueError:
            print("Invalid input try again")
            continue
        temp_lt.append((item_no, quantity))
        temp[item_no] = quantity
        print("do you want to enter more items y/n?".upper())
        uio = input("-->")
        if uio.upper() != "Y":
            break

    if typ:
        return temp_lt
    elif not typ:
        return temp
    else:
        return


def gen_bill():
    prev_bill_no = [i[0] for i in view_table("sales")]
    bi = bill()
    all_dat = out_rec_dict(bi)
    actual_rec = []
    current_bill_no = max(prev_bill_no) + 1
    for i in all_dat:
        ttl = (current_bill_no, date.today(), i[0], i[1], bi[i[0]], i[5], "10",
               int((int(bi[i[0]]) * int(i[5])) + (((int(bi[i[0]]) * int(i[5])) / 100) * 10) // 1))
        actual_rec.append(ttl)
    display_record = align_records_with_head(actual_rec, "sales")[2:]
    print(f"BILL NO : {current_bill_no} ")
    print(f"Date : {date.today()}")
    for i in field_to_row(display_record):
        for j in i:
            print(j, end='| ')
        print()
    print(f"TOTAL AMOUNT = Rs {sum([int(i) for i in display_record[-1][1:]])}")
    input_data("sales", actual_rec)

vtrl = 0

while not vtrl:
    print("1. NEW BILL\n"
          "2. INVENTORY\n"
          "3. VIEW SALES HISTORY\n"
          "4. EXIT")
    try:
        win = int(input("--->"))
    except ValueError:
        print("INVALID INPUT")
        continue
    if win == 1:
        gen_bill()
    elif win == 2:
        take_control("INVENTORY")
    elif win == 3:
        take_control("SALES")
    elif win == 4:
        vtrl = 1
    else:
        print("INVALID INPUT")


