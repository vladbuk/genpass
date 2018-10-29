from genpass_class import Genpass
from sys import argv

def main(argv):
    try:
        length = int(argv[1])
        power = int(argv[2])
    except IndexError:
        # if no arguments in command line added
        print('Default arguments used')
        length = 12
        power = 2

    pass1 = Genpass(length, power)

    for _ in range(10):
        print(pass1)

if __name__ == "__main__":
   main(argv)
   input('Press "Enter" to exit')
