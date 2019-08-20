# python 
# Linhe Sun
# for practice 9-10
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is a(n) " + self.cuisine_type + 
            " restaurant.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now.")
        
    def set_number_served(self, sv_number):
        if sv_number >= self.number_served:
            self.number_served = sv_number
        print(str(self.number_served) + " people are served.")
    
    def increment_number_served(self, in_number):
        if in_number >= 0:
            self.number_served += in_number
        print(str(self.number_served) + " people are served.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = ['strawberry', 'chocolate', 'apple']
        
    def describe_icecreams(self):
        print("We have these kinds of icecreams:")
        for flavor in self.flavors:
            print("    - " + flavor)