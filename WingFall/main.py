from characters import luma
from locations import locations

print("Wingfall")
print(f"You are {luma['name']}, a {luma['species']}.")

current_location = luma["location"]
print(f"Your starting location is: {current_location}")
print(f"Description: {locations[current_location]['description']}")