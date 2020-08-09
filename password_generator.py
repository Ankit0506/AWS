from random import choice

len_of_password = 8
valid_chars = "abcdefgf1234@"

password=[]
for each_char in range(len_of_password):
    password.append(choice(valid_chars))
random_pass="".join(password)
print(random_pass)

