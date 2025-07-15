import random

adjectives = ['Caterpillar', 'Beetle', 'Spider', 'Larva', 'Ant', 'Weevil', 'Moth']
roles = ['Wizard', 'Knight', 'Chef', 'Ninja', 'Pirate', 'Detective', 'Queen']

bug_title = f"{random.choice(adjectives)} {random.choice(roles)}"
print(f"\n A new bug character has arrived: **{bug_title}**!")

name = input("What will you name them? ")

print(f"\n {bug_title} shall now be known as... **{name}**!")
print(f"{name} off into the grass on a brave adventure.")