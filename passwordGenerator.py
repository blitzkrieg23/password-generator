import random
import re

alphanumeric_pattern = re.compile(r'\w')
password_length = 8
password = ''

for i in range(password_length):

    password += random.choice(re.findall(alphanumeric_pattern, 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))

print(password)