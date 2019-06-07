import string
import random

uname = input("Enter username:\n")
print("Saving to file...")

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(10, 20)
  return ''.join(random.choice(chars) for x in range(size))

filename = uname+'.txt'

with open(filename, 'a') as out:
    out.write("Username: " + uname + '\n')
    out.write("Password: " + randompassword() + '\n')
