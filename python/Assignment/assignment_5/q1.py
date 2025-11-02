# 1. Write a program to prompt user to enter userid and password. If Id and  
# password is incorrect give him chance to re-enter the credentials. Let him try 3  
# times. After that program to terminate.

# Set credentials
correct_id = "Ganesh9527"
correct_pw = "ganesh@123"

# Give user 3 chances
for attempt in range(1, 4):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_pw:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials! Try again.")
        print("Attempts left:", 3 - attempt)
        print()

# If all 3 attempts are used
else:
    print("3 incorrect attempts...! Access fail...")
