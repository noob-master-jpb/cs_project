from database import *


def count_row_len(ind, table):  # used to count the max length of a value in a field and returns it
    all = view_table(table)
    lt = 0
    for i in all:
        i = str(i[ind])
        if len(i) > lt:
            lt = len(i)
    return lt


def align_field_table(id, table):  # used to align the values in field
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


def ret_header(table):  #returns the header list of the table
    tem = []
    for c in table_structure(table):
        tem.append(c[0])
    return tem


def align_row_head(lis, table):  # takes rows and return aligned rows
    temp = []
    max_lis = []
    tem = []  # not works if multiple fields in the record has same value
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


def field_to_row(lis):  # works as same as name
    temp = []
    for j in range(0, len(lis[0])):
        t = []
        for i in lis:
            t.append(i[j])
        temp.append(t)
    return temp


def align_records_with_head(records, table):  # aligns the records with proper field names from specific table
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
