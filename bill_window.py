# class Item:
#     def __init__(self, item_id, name, price):
#         self.id = item_id
#         self.name = name
#         self.price = price
#
#
#
# def take_customer_info():
#     name = input('Name: ')
#     address = input('Address: ')
#     return name, address
#
#
#
#
# #ctrl = 0
# #while by ctrl
#
# def take_item_list():
#     total_items = int(input('Enter the total number of items: '))
#     items = []
#     for i in range(total_items):
#         item_id = i + 1
#         name = input('Enter item name: ')
#         price = int(input('Enter price: '))
#         items.append(Item(item_id, name, price))
#     return items
#
#
# def display_bill(items, customer_name, customer_address):
#     total = 0
#     print('\n\n\n')
#     print('\t       Store       ')
#     print('\t -----------------')
#     print(f"Name : {customer_name} \t Address : {customer_address}")
#     for obj in items:
#         print(f'Id : {obj.id}\tItemName : {obj.name}\tPrice : {obj.price}')
#         print('----------------------------------------------------')
#         total += obj.price
#     print(f'\t\tTotal : {total}')
#     print('\tThanks for visiting')
#     print('\n\n')
#
#
# # Main program
# customer_name, customer_address = take_customer_info()
# item_list = take_item_list()
# display_bill(item_list, customer_name, customer_address)

item_name = []

