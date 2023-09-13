import os
import bcrypt
from dotenv import load_dotenv

# Step 1: Load the 'pepper' (AUTH_PEPPER) from .env
# The 'pepper' is an additional environmental variable
# that can be appended onto the password pre-salt & hash

load_dotenv()
pepper = os.environ.get("AUTH_PEPPER")
print("\nStep 1: Generate pepper from .env")
print(f"Generated pepper {pepper}")


# Step 2: Generate salt (randomized string) to append to
# userpassword prior to hash

print("\nStep 2: Generate salt (random string) to append to"
      " user password pre-hash")
salt = bcrypt.gensalt()
print(f"Generated salt: {salt}")

# Step 3: Access user password, add salt and pepper, hash

print("\nStep 3: Add salt and pepper to user password and hash")
my_password = "abc123"+pepper
hash_pass = bcrypt.hashpw(my_password.encode('UTF-8'),salt)
print(f"User pass + pepper: {my_password}")
print(f"Hashed password: {hash_pass}")

# Step 4: Request password from user and apply pepper

print("\nStep 4: Request user password and append pepper to input")
user_pass = input("Please input your password : ")
pepper_pass = f"{user_pass}{pepper}"
print(f"\nUser pass + pepper: {pepper_pass}")

# Step 5: Validate password 

print("\nStep 5: Validate password")
if bcrypt.checkpw(pepper_pass.encode('UTF-8'), hash_pass):
    print("Password successful. Access granted.")
else:
    print("Incorrect password. Access denied.")

