from Item import Item

class Store:
    
    def __init__(self):
        self.store = {}
        
    def addItem(self, item):
        if item.category not in self.store:
            self.store[item.category] = [item]
        else:
            self.store[item.category].append(item)
            
    def removeItem(self, item):
        for index, store_item in enumerate(self.store.get(item.category, [])):
            if store_item.upc == item.upc:
                self.store[item.category].pop(index)
                break
            
    def removeCategory(self, category):
        if category.upper() in self.store:
            removed_items = self.store.pop(category.upper())
            removed_items_str = ''
            for item in removed_items:
                removed_items_str += item.toString()+ '\n'
            return removed_items_str.strip()
        else:
            return False
        
    def getItems(self, category):
        category_str = ''
        if category.upper() not in self.store: # Returns empty string if category is not in Store
            return ''
        for index, items in enumerate(self.store[category.upper()]):
            item_info_string = items.toString()
            category_str += item_info_string + '\n'
        return category_str.strip()

    def doesItemExist(self, item):
        for index, store_item in enumerate(self.store.get(item.category, [])):
            if store_item.upc == item.upc:
                return True # will return True once/if it finds a upc that matches
        return False # otherwise returns False

    def countDollarItems(self):
        dollar_list = []
        for value in self.store.values():
            for items in value:
                if items.price == None: # If there is no price, with item, do nothing
                    continue
                elif items.price <= 1.0: # If price is int or float adds if less than or equal to 1
                    dollar_list.append(items)
        return len(dollar_list)
