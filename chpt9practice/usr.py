#python
# Linhe Sun
# for practice 9-11
class User():
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
        self.login_attempts = 0
        
    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + 
            " is a user of our production.")
    
    def greet_user(self):
        print("Hi " + self.first_name.title() + ", welcome back!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

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