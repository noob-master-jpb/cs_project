from sqlite3 import *

connection = Connection("main_data")
control = connection.cursor()


# sales_att = list(control.execute("""Pragma table_info(sales_table)"""))[-1][0] + 1
# inv_att = list(control.execute("""Pragma table_info(inventory_table)"""))[-1][0] + 1
# except IndexError:
#     print('')
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
    return list(control.execute("""Pragma table_info(""" + table + """)"""))[-1][0] + 1


def execute(st):
    return control.execute(st)


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


def input_data(table, lis=[]):
    if not lis:
        print("NO INPUT")
        return
    field_ctrl = '?,' * att_no(table)
    control.executemany("""INSERT INTO """ + table + """ VALUES (""" + field_ctrl[:-1] + """)""", lis)


def table_structure(table):
    return list(control.execute("""Pragma table_info(""" + table + """)"""))


def view_table(table=''):
    if table == '':
        print("NO TABLE NAME GIVEN")
    control.execute(("""SELECT * FROM """ + table + """;"""))
    print(control.fetchall())
    return control.fetchall()


def show_tables(self):
    temp = []
    for i in control.execute("""select name from sqlite_schema where type = 'table'"""):
        temp.append(i[0])
    return temp

print()