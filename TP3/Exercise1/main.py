from Inventory import Inventory

class main(object):
    if __name__ == "__main__":
        inventory = Inventory()

        inventory.add_item('I001', 'Laptop', 100, 500.00)
        inventory.add_item('I002', 'Mobile', 110, 450.00)
        inventory.add_item('I003', 'Desktop', 120, 500.00)
        inventory.add_item('I004', 'Tablet', 90, 550.00)

        print('Item details: ')
        print(inventory.check_item_detail('I001'))
        print(inventory.check_item_detail('I002'))
        print(inventory.check_item_detail('I003'))
        print(inventory.check_item_detail('I004'))

        print()

        print('Update price of item - \'I001\': ')
        inventory.update_item('I001', price=505.00)
        print(inventory.check_item_detail('I001'))
        print('Update stock of item - \'I003\': ')
        inventory.update_item('I003', 115, 505.00)
        print(inventory.check_item_detail('I003'))
