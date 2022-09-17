""" ** Password Picker **


Pick secure and hard to guess password.
This program generates easy to remember
yet hard to crack passwords for you.

    Name : Yash Vyavahare
    mail : yashvyawahare02@gmail.com
"""


# import library
import random

# set some names as you wish
adjectives = ['quick', 'slow', 'hot', 'sexy']
words      = ['jorina', 'cow', 'lip']

# now we generate new password randomly
password = random.choice(adjectives) + random.choice(words) + str(random.randint(0, 100))

print(password)