import string
import random
import time
print("=========================password generator=========================")
time.sleep(1)
print("working on it",end="")
for i in range(3):
    time.sleep(1)
    print(".",end="")
time.sleep(1)
print()
pool = string.ascii_lowercase + string.ascii_uppercase + string.digits
password = ""
for _ in range(8):
    password += random.choice(pool)

print(f"horriay! your password is ready! use it wise: {password}")
