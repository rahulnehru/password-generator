import string
import random

user_name = input("Enter username:\n")
print("Saving to file...")

def random_password():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(random.randint(10, 20)))

filename = user_name + ".txt"

with open(filename, "a") as out:
    out.write("Username: " + user_name + '\n')
    out.write("Password: " + random_password() + '\n')
