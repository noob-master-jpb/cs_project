from datetime import *

from pymysql import *

# code with minimum debugging _______
connection = Connect(
    host="localhost",
    user='root',
    password="root",
    db="project_main"
)
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


def input_data(table, lis=[525]):
    if not lis:
        print("NO INPUT")
        return
    field_ctrl = '%s,' * att_no(table)
    control.executemany("""INSERT INTO """ + table + """ VALUES(""" + field_ctrl[:-1] + """)""", lis)
    connection.commit()
