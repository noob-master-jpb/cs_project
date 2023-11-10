from database import *


def count_row_len(ind, table):  # used to count the max length of a value in a field and returns it
    all = view_table(table)
    lt = 0
    for i in all:
        i = str(i[ind])
        if len(i) > lt:
            lt = len(i)
    return lt


def align_field(id, table):  # used to align the values in field
    temp = []
    for i in view_table(table):
        k = i[id]
        if len(str(k)) < count_row_len(id, table):
            k = ' ' * (count_row_len(id, table) - len(str(k))) + str(k)
        temp.append(k)

def align_field_head(id, table):  # used to align the values in field
    temp = []
    tem = []
    for c in table_structure(table):
        tem.append(c[0])
    for i in view_table(table):
        k = i[id]
        if len(str(k)) < len(tem[id]):
            k = ' ' * (len(tem[id]) - len(str(k))) + str(k)
        temp.append(k)
    return temp

def align_row(lis, table):  # takes rows and return aligned rows
    temp = []
    max_lis = []
    for j in range(0, att_no(table)):
        max_lis.append(count_row_len(j, table))
    for ko in lis:
        ti = []
        for i in ko:
            k = i
            if len(str(k)) < max_lis[ko.index(i)]:
                k = ' ' * (max_lis[ko.index(i)] - len(str(k))) + str(k)
            ti.append(k)
        temp.append(ti)
    return temp


def ret_header(table):
    tem = []
    for c in table_structure(table):
        tem.append(c[0])
    return tem


def align_row_head(lis, table):  # takes rows and return aligned rows
    temp = []
    max_lis = []
    tem = []                # not works if multiple fields in the record has same value
    for c in table_structure(table):
        tem.append(c[0])
    # print(tem)
    for j in range(0, att_no(table)):
        max_lis.append(len(tem[j]))
    for ko in lis:
        ti = []
        for i in ko:
            k = i
            if len(str(k)) < max_lis[ko.index(i)]:
                k = ' ' * (max_lis[ko.index(i)] - len(str(k))) + str(k)
            ti.append(k)
        temp.append(ti)
    return temp

def field_to_row(lis):

