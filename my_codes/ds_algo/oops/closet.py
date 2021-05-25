"""
1. The Closet Object has the following attributes:
length: length of the closet in feet
breadth: breadth of the closet in feet
height: breadth of the closet in feet
max_capacity: Total number of items that a closet supports
items: The list of items in the closet. [All strings]
2. The Closet Object supports the following methods:
store_item(): Takes a string as input and adds it to the items list
fetch_item(): Returns the frontmost object in the items list

"""

class Closet():

    def __init__(self, length, breadth, height, max_capacity, items):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.max_capacity = max_capacity
        self.items = items
    
    def store_item(self):
        new_item = input("Please enter an item : ")
        self.items.append(new_item)
        return self.items
    
    def fetch_item(self):
        return self.items[0]



my_closet = Closet(6,5,12,25,['Bottle','Pants','Shirts','Keys','Bedsheet'])

# uncomment below line to check the class attributes
# print(f"The length of the closet in feet is {my_closet.length} ft. ")
# print(f"The breadth of the closet in feet is {my_closet.breadth} ft. ")
# print(f"The height of the closet in feet is {my_closet.height} ft. ")
# print(f"Total number of items that this closet supports is : {my_closet.max_capacity} ")
# print(f"The list of items in the closet are : {my_closet.items} ")

# uncomment below line to check the class attributes
# print(my_closet.store_item())
# print(my_closet.fetch_item())
