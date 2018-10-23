from genpass_class import Genpass

# create Genpass object
pass1 = Genpass(16)

# get one password with length=16 with upper letters, lower letters, numbers and symbols
print('pass:', pass1.getPass())


# get ten simple 8 chars passwords
pass2 = Genpass(8, 0)

for n in range(10):
    print('pass {}: {}'.format(n, pass2))
    # or classic
    # print(pass1.getPass())