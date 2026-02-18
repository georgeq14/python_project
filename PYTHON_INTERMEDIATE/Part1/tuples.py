"""
Tuples are ordered collections that cannot be changed after creation.

This means that they are immutable, which means their values cannot change. 
They’re great for data that should stay the same, like coordinates or color values.

"""
"""
#example tuples
person = ('Kat', 24)
navy_blue = (0, 0, 128)
# Note: if there is only one item, make sure there is a comma
"""

"""
Ian = ("14.41", "121.05")
Gen = ("14.16", "121.24")
Drake = ("18.67", "121.23")

print(Ian)
print(Gen)
print(Drake)
"""

friend1_location = (37.7749, -122.4194)   # San Francisco
friend2_location = (40.7128, -74.0060)    # New York
friend3_location = (4.624335, -74.063644) # Bogota

# Bonus: Accessing Tuple Elements
print("Latitude and Longitude of the furthest friend's location:", friend1_location)

all_friends_locations = friend1_location + friend2_location + friend3_location

print("All friends' locations combined:", all_friends_locations)

