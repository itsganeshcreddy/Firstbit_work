# a program to prompt user to enter userid and password. After verifying 
# userid and password display a 4 digit random number and ask user to enter the 
# same. If user enters the same number then show him success message otherwise 
# failed. (Something like captcha)
import random
uid = 'ganesh'
passd = 'ganesh@123'

user_id = input("Enter userid:")
user_pass = input("Enter password:")

if(uid == user_id and passd == user_pass):

    captcha = random.randint(1111,9999)
    print("Captcha:",captcha)
    user_captcha = int(input("Enter the captcha shown above:"))

    if(user_captcha == captcha):
        print("logged in succesfully.")
    else:
        print("Captcha not matched.")    
else:
    print("wrong userid and password.")