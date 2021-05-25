"""
1. The Bed Object has the following attributes:
length: length of the bed in feet
breadth: breadth of the bed in feet
year_made: Year in which the bed was made
has_headboard: True or False depending on whether the bed has a headboard or not
has_posts: True or False depending on whether the bed has sideposts or not
material: material is wood, steel, plywood and so on.
2. The Bed Object does not support any following methods

"""

class Bed(): # Beds class made with followings attributes
    def __init__(self,length,breadth,year_made,has_headboard,has_posts,material):
        self.length = length
        self.breadth = breadth
        self.year_made =  year_made
        self.has_headboard = has_headboard
        self.has_posts = has_posts
        self.material = material

my_bed = Bed(10,5,2015,True,False,'Wood')

# for checking just uncomment below lines

print(f"The length of the bed in feet is : {my_bed.length} feet ")
print(f"The breadth of the bed in feet is {my_bed.breadth} feet ")
print(f"The bed is made in the year of : {my_bed.year_made} ")
print(f"This bed has headboard : {my_bed.has_headboard} ")
print(f"This bed has posts : {my_bed.has_posts} ")
print(f"The materials that use to make the bed is : {my_bed.material}")
