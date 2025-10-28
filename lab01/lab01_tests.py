from Item import Item
from Store import Store

ex_item = Item(upc=420012347654, category="PRODUCE", name="AVOCADO", price=2.0)
ex_item_2 = Item(upc=2, category="PRODUCE", name="BANANAS", price=0.79)
ex_item_3 = Item(upc=3, category="PRODUCE", name="CILANTRO", price=0.99)
ex_store = Store()
ex_store.addItem(ex_item)
ex_store.addItem(ex_item_2)
ex_store.addItem(ex_item_3)
# print(ex_store.getItems('PRODUCE'))
print(ex_store.removeCategory('PRODUCE'))
