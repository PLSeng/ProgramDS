class Inventory(object):
    def __init__(self):
        self.Inventory = {}

    def add_item(self, itemID, itemName, quantity, price):
        """
        TODO: Add item to inventory

        :param itemID:
        :param itemName:
        :param quantity:
        :param price:
        :return:
        """
        self.Inventory[itemID] = {
            'itemName': itemName,
            'quantity': quantity,
            'price': price
        }

    def update_item(self, itemID, quantity=None, price=None):
        if itemID in self.Inventory:
            if quantity is not None:
                self.Inventory[itemID]['quantity'] = quantity
            if price is not None:
                self.Inventory[itemID]['price'] = price
            print('Update successful')
        else:
            print("Item not found")
    def check_item_detail(self, itemID):
        """
        TODO: Check item details
        :param itemID:
        :return:
        """
        if itemID in self.Inventory:
            return f'Item Name: {self.Inventory[itemID]["itemName"]}, Quantity: {self.Inventory[itemID]["quantity"]}, Price: {self.Inventory[itemID]["price"]}'
        else:
            return 'Item not found'