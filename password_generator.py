"""
1.Write a function that takes n number of characters to generate a password
2.The password will have ascii-letters, digits, and punctuations
   i. We start by importing the random and string modules
   ii. We then define the function.
   iii. Using the method string, we access ascii letters, digits, and punctuations, concatenate them and store them in a variable called characters.
   iv.With an empty separator, we use the join method and randomly choose the characters and repeat the process in n iteration
   v. return password, which will be a string of different characters.
"""
import random
import string

def password_generator(n):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for i in range(n))
        return password

print(password_generator(12))