#  check if user has entered correct userid and password.

uid = 'ganesh'
passd = 'ganesh@123'

user_id = input("Enter userid:")
user_pass = input("Enter password:")

if(uid == user_id and passd == user_pass):
    print("logged in succesfully.")
else:
    print("wrong userid and password.")