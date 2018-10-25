from genpass_class import Genpass
from sys import argv

def main(argv):
    length = int(argv[1])
    power = int(argv[2])

    pass1 = Genpass(length, power)

    for _ in range(10):
        print(pass1)

# main(argv)

if __name__ == "__main__":
   main(argv)
#    main(argv[1:])