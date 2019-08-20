#python
# Linhe Sun
# for practice 9-12
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
