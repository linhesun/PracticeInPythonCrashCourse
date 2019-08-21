# Chapter 11 practice
# Linhe Sun

# practice 11-1
# city_functions.py
def city_function(city, country):
    result = city.title() + ', ' + country.title()
    return result

# test_cities.py
import unittest
from city_functions import city_function

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formated_city = city_function('beijing', 'china')
        self.assertEqual(formated_city, 'Beijing, China')

unittest.main()

# practice 11-2
# city_functions.py---version1
def city_function(city, country, population):
    result = city.title() + ', ' + country.title() + ' - population ' + str(population)
    return result
# city_functions.py---version2
def city_function(city, country, population=''):
    if population:
        result = city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        result = city.title() + ', ' + country.title()
    return result
# test_cities.py---modified
import unittest
from city_functions import city_function

class CityTestCase(unittest.TestCase):
    
    def test_city_country(self):
        formated_city = city_function('beijing', 'china')
        self.assertEqual(formated_city, 'Beijing, China')
        
    def test_city_country_population(self):
        formated_city  = city_function('beijing', 'china', 20000000)
        self.assertEqual(formated_city, 'Beijing, China - population 20000000')
        
unittest.main()

# practice 11-3
# employee.py
class Employee():
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary
    
    def give_raise(self, increace=5000):
        self.salary += increace
# test_employee.py----version1
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_give_default_raise(self):
        my_test = Employee('Linhe', 'Sun', 2000)
        my_test.give_raise()
        self.assertEqual(my_test.salary, 7000)

    def test_give_custom_raise(self):
        my_test = Employee('Linhe', 'Sun', 2000)
        my_test.give_raise(6000)
        self.assertEqual(my_test.salary, 8000)
    
unittest.main()
# test_employee.py----version2
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_test = Employee('Linhe', 'Sun', 2000)
        self.increace = 6000
    
    def test_give_default_raise(self):
        self.my_test.give_raise()
        self.assertEqual(self.my_test.salary, 7000)

    def test_give_custom_raise(self):
        self.my_test.give_raise(self.increace)
        self.assertEqual(self.my_test.salary, 8000)
    
unittest.main()

