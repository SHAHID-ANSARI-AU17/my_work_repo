"""
1. The Bedroom object has the following attributes:
• length: length of the room in feet
• breadth: breadth of the room in feet
• height: breadth of the room in feet
• bed: an object representing the bed in the bedroom. Initialize as None.
• closet: an object representing the closet in the bedroom. Initialize as
None.
• has_balcony: True or False depending on whether the room has a balcony or
not
• has_window: True or False depending on whether the room has a window or
not
• num_lights: The number of lights/lightsockets in the number
• has_ac: True or False depending on whether the room has a window or not
• has_fan: True or False depending on whether the room has a window or not
• num_charging_points: Number of charging points in the room.

2. The Bedroom object has the following methods:
• carpet_area(): Returns the carpet area of the room which is calculated as
length*breadth

• add_bed(): creates a Bed object using user inputs [using input() function]
and assigns it to the bed attribute of the bedroom. While adding a bed
make sure the dimensions of the bed are suitable for the remaining carpet
area in the room.
For example: you cannot add a 9x9 bed in a 8X10 bedroom
For example 2: you cannot add a 6x3 bed in a 8x10 bedroom if there is
already a closet which takes up 60 sq ft space.

• add_closet(): creates a Closet object using user inputs [using input()
function] and assigns it to the closet attribute of the bedroom. While
adding a close make sure the dimensions of the closet are suitable for the
remaining carpet area in the room.
For example: you cannot add a 9x9 closet in a 8X10 bedroom
For example 2: you cannot add a 6x3 closet in a 8x10 bedroom if there is
already a bed which takes up 60 sq ft space.

• remove_bed(): Checks if the bed attribute is None. If not, then makes it
None and returns “bed removed from the room”. If bed attribute is already
None, then it returns “No bed found in the room”.

• remove_closet(): Checks if the closet attribute is None. If not, then
makes it None and returns “closet removed from the room”. If closet
attribute is already None, then it returns “No closet found in the room”.

"""

class Bedroom(): # these are attributes
    def __init__(self,length,breadth,height,bed,closet,has_balcony,has_window,num_lights,has_ac,has_fan,num_charging_points):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.bed = bed
        self.closet = closet
        self.has_balcony = has_balcony
        self.has_window = has_window
        self.num_lights = num_lights
        self.has_ac = has_ac
        self.has_fan = has_ac
        self.num_charging_points = num_charging_points
        self.effective_carpet_area = 0 # additional attribute
        # self.carpet_area = carpet_area # additional attribute

    
    def carpet_area(self):
        print("-----------carpet area-----------")
        return self.length*self.breadth
    
    def add_bed(self):
        print("-----------add bed-----------")
        length_of_bed = int(input('Enter the length of the bed in ft : '))
        breadth_of_bed = int(input('Enter the breadth of the bed in ft : '))
        bed_area = length_of_bed*breadth_of_bed
        
        # carpet_area = self.carpet_area() 
        # if self.carpet_area() > bed_area:
        #     self.effective_carpet_area = (self.carpet_area() - bed_area)
        #     print(f"Bed is added in the bedroom.")
        #     print(f"Total bed area is {bed_area} sq. ft. ")
        #     self.bed = True
        #     return (f"Total Bedroom area was {self.carpet_area()} sq. ft. and bed area is {bed_area} sq. ft. Now the remaining bedroom area is {self.effective_carpet_area()} sq. ft. ")


    def add_closet(self):
        print("-----------add closet-----------")
        length_of_closet = int(input('Enter the length of the closet in ft : '))
        breadth_of_closet = int(input('Enter the breadth of the closet in ft : '))
        closet_area = (length_of_closet*breadth_of_closet)
        # remaining_area = 
        # self.carpet_area = remaining_area - closet_area
        if self.effective_carpet_area > closet_area:
            print(f"Closet is added in the bedroom.")
            print(f"Total closet area is {closet_area} sq. ft. ")
            self.closet = True
            return (f"Total Bedroom area was {self.effective_carpet_area} ft. and closet area is {closet_area} ft. Now the remaining bedroom area is {self.self.effective_carpet_area-closet_area}")

    def remove_bed(self):
        print("-----------remove bed-----------")
        if self.bed != None:
            self.bed = None
            return  "bed removed from the room"

        if self.bed==None:
            return "No bed found in room"
    

    def remove_closet(self):
        print("-----------remove closet-----------")
        
        if self.closet != None:
            self.closet = None
            return  "closet removed from the room"
        
        if self.closet==None:
            return "No closet found in room"
        


    

my_bedroom = Bedroom(25,20,15,None,None,True,True,15,False,True,5)

# uncomment below line to check the code

# print(f"The length of the bedroom is {my_bedroom.length} feet")
# print(f"The breadth of the bedroom is {my_bedroom.breadth} feet ")
# print(f"The height of the bedroom is {my_bedroom.height} feet")
# print(f"The bed in the bedroom is {my_bedroom.bed} ")
# print(f"The closet in the bedroom is {my_bedroom.closet} ")
# print(f"The room has a balcony : {my_bedroom.has_balcony}")
# print(f"The room has a window : {my_bedroom.has_window}")
# print(f"The number of lights/lightsockets is {my_bedroom.num_lights}")
# print(f"The room has ac : {my_bedroom.has_ac}")
# print(f"The room has fan : {my_bedroom.has_fan}")
# print(f"Number of charging points in the room are {my_bedroom.num_charging_points}")

# uncomment below line to check the method
print(f"The total carpet area of the bedroom is {my_bedroom.carpet_area()} sq ft.")


# ----- line 140 and 141 should be check together -----
print(my_bedroom.add_bed()) 
print(f"The total carpet area of the bedroom is {my_bedroom.carpet_area()} sq ft.")


# print(my_bedroom.add_closet())

# print(my_bedroom.remove_bed())
# print(my_bedroom.remove_closet())
