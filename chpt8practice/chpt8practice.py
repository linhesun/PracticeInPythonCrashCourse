#Chapter 8 practice
# Linhe Sun

# practice 8-1
def display_message():
    print("In this chapter, we will study how to use functions in Python.")

display_message()

# practice 8-2
def favorite_book(title):
    print("One of my favorite books is " + title.title() + ".")

favorite_book('alice in wonderland')

# practice 8-3
def make_shirt(size, logo):
    print("I will make a " + str(size) + " size shirt with the logo '" + logo +
        "' on it.")
make_shirt(7, 'LOVE & PEACE')
make_shirt(logo = 'LOVE & PEACE', size = 7)

# practice 8-4
def make_shirt(size = 'L', logo = 'I Love Python'):
    print("I will make a " + str(size) + " size shirt with the logo '" + logo +
        "' on it.")
make_shirt()
make_shirt('M')
make_shirt(logo = 'MAKE LOVE NOT WAR')

# practice 8-5
def describe_city(city, country = 'China'):
    print(city.title() + " is in " + country.title() + ".")
describe_city('hong kong')
describe_city('beijing')
describe_city('tokyo', 'japan')

# practice 8-6
def city_country(city, country):
    citycountry = '"' + city.title() + ', ' + country.title() + '"'
    return citycountry
print(city_country('beijing', 'china'))

# practice 8-7
def make_album(singer_name, album_name):
    albuminfo = {'Singer': singer_name, 'Album': album_name}
    return albuminfo
print(make_album('Coldplay', 'X&Y'))
print(make_album('New Pants', 'GO EAST'))
print(make_album('My Chemical Romance', 'The Black Parade'))

def make_album(singer_name, album_name, track_num='NONE'):
    if track_num.isdigit():
        albuminfo = {'Singer': singer_name, 'Album': album_name, 
            'Tracks': int(track_num)}
    else:
        albuminfo = {'Singer': singer_name, 'Album': album_name}
    return albuminfo
print(make_album('Coldplay', 'X&Y', '19'))
print(make_album('New Pants', 'GO EAST', 'NA'))
print(make_album('My Chemical Romance', 'The Black Parade'))

# practice 8-8
def make_album(singer_name, album_name):
    albuminfo = {'Singer': singer_name, 'Album': album_name}
    return albuminfo
while True:
    print("Type q to quit anytime")
    singer = input("Please type a singer/band's name:\n")
    if singer == 'q':
        break
    album = input("Now type one album name of the singer/band:\n")
    if album == 'q':
        break
    print(make_album(singer, album))

# practice 8-9
magicians = ['David', 'Qian Liu', 'Yandong Fu']
def show_magicians(magicians):
    for magician in magicians:
        print("This magician is " + magician + ".")
show_magicians(magicians)

# practice 8-10
magicians = ['David', 'Qian Liu', 'Yandong Fu']
def show_great(magicians):
    for magician in magicians:
        great = magicians.pop(0) + " the Great"
        magicians.append(great)
    return magicians
print(show_great(magicians))
print(magicians)

# practice 8-11
# 2 ways
# 1st
magicians = ['David', 'Qian Liu', 'Yandong Fu']
def show_great(magicians):
    greats = []
    for magician in magicians:
        great = magician + " the Great"
        greats.append(great)
    return greats
print(show_great(magicians))
print(magicians)
# 2nd
magicians = ['David', 'Qian Liu', 'Yandong Fu']
def show_great(magicians):
    for magician in magicians:
        great = magicians.pop(0) + " the Great"
        magicians.append(great)
    return magicians
print(show_great(magicians[:]))
print(magicians)

# practice 8-12
def make_sanwichs(*insides):
    print("\nYou want a sanwich with these inside:")
    for inside in insides:
        print("    -" + inside.title())
make_sanwichs('chicken')
make_sanwichs('beef', 'chicken', 'egg')
make_sanwichs('tomato', 'cucumber', 'egg', 'chicken')

# practice 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
my_profile = build_profile('Linhe', 'Sun', 
    location = 'Beijing',
    field = 'genetics')
print(my_profile)

# practice 8-14
def make_car(band, type, **other_info):
    car_info = {}
    car_info['band'] = band
    car_info['type'] = type
    for key, value in other_info.items():
        car_info[key] = value
    return car_info
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

# practice 8-15
# see printing_functions.py

# practice 8-16
# function part see: chi_square.py
# main part see: test_chi.py

# practice 8-17
# the body of practice 8-5
def describe_city(city, country = 'China'):
    print(city.title() + " is in " + country.title() + ".")
# it should be 
def describe_city(city, country='China'):
    print(city.title() + " is in " + country.title() + ".")
