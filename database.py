from datetime import *

from pymysql import *

# code with minimum debugging _______
connection = Connect(host="localhost",user='root',password="root",db="project_main")
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



def att_no(table): # number of fields describe
    return control.execute("""describe """ + table)


def view_table(table=''): # records without attribute list of tuples return kore
    if table == '':
        print("NO TABLE NAME GIVEN")
    control.execute(("""SELECT * FROM """ + table + """;"""))
    return control.fetchall()


def table_structure(table=''): # desc table
    if table == '':
        print("NO TABLE INPUT")
        return
    control.execute(f'describe {table}')
    return control.fetchall()


def input_data(table, lis=[]): #input records in list of tuples
    if not lis:
        print("NO INPUT")
        return
    field_ctrl = '%s,' * att_no(table)
    control.executemany("""INSERT INTO """ + table + """ VALUES(""" + field_ctrl[:-1] + """)""", lis)
    connection.commit()

def reset_table(table=''): # new table creation or exiting table reset using drop
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
    k =[]
    for i in a.keys():
        control.execute(f"select * from inventory where item_no = {i};")
        k.append(control.fetchall()[0])
    return k

def out_fields_tab(feild = None,tab = None):
    if (not feild) or (not tab):
        return
    control.execute(f"select {feild} from {tab}")
    return control.fetchall()