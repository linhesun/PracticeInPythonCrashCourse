#python
# Linhe Sun
# for practice 9-12
from user import User
class Previleges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self, nums=[2]):
        for num in nums:
            print("This admin " + self.privileges[num] + ".")
    
class Admin(User):
    def __init__(self, first, last):
        super().__init__(first, last)
        self.previleges = Previleges()