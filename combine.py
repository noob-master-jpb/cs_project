from function_set import *
from database import *


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
    elif tab.upper() == "SALES":
        ls = ["QUANTITY", "PRICE", "TOTAL", 'BILL_DATE']
    else:
        print("table not included in function".upper())

    for i in enumerate(ls):
        print(f"{i[0] + 1}. by {i[1].replace('_', ' ')}")

    ap = int(input("--> "))

    print(f"PUT THE RANGE OF {ls[ap - 1].replace('_', ' ')}")
    up = input("FROM--> ")
    down = input("TO--> ")

    if ls[ap] not in ls[-2:]:
        up = int(up)
        down = int(down)

    # print(f"SELECT * FROM {tab} WHERE {ls[ap-1]} BETWEEN {up} AND {down};".upper())
    print(control.execute(f"SELECT * FROM {tab} WHERE {ls[ap - 1]} BETWEEN {up} AND {down};".upper()), "RECORDS FOUND")
    filt_data = control.fetchall()
    show_table(filt_data, tab)
    return filt_data


def take_control(tab):
    header = ret_header(tab)
    all_rec = view_table(tab)
    tt = show_table(view_table(tab), tab)
    ctrl = 0
    print("ALL RECORDS")
    while not ctrl:
        print("1. To USE FILTER")
        print("2. To USE SORTING")
        print("3. To CLOSE")

        at = int(input("--> "))
        if at == 1:
            temp_data = filter(tab)
            # print(temp_data)
            print("DO YOU WANT TO SORT THIS TABLE? y/n")
            sr = input("-->")
            if sr.upper() == 'Y':
                for i in enumerate(header):
                    print(f"{i[0] + 1}. by {i[1].replace('_', ' ')}")
                srt = int(input("-->"))
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
                # print(sort_seq)
                show_table([temp_data[i] for i in sort_seq], tab)
        elif at == 2:
            for i in enumerate(header):
                print(f"{i[0] + 1}. by {i[1].replace('_', ' ')}"),
            srt = int(input("-->"))
            print("1. ascending".upper())
            print("2. Descending".upper())
            srt_type = int(input("-->"))
            sort_seq = sort_field_seq(srt - 1, tab)
            if srt_type == 2:
                sort_seq.reverse()
            elif srt_type == 1:
                print()
            else:
                print("invalid input".upper())
            # print(sort_seq)
            show_table([view_table(tab)[i] for i in sort_seq], tab)
        elif at == 3:
            ctrl = 1
