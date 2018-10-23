import random

class Genpass(object):
    
    """ Generate password with specific length and strong """
    
    __numbers = [chr(x) for x in range(48, 58)]
    __symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    __lower_letters = [chr(x) for x in range(97, 123)]
    __upper_letters = [chr(x) for x in range(65, 91)]

    # strong = 0 or 1 or 2
    def __init__(self, length=12, strong=2):
        self.length = length
        self.strong = strong

    
    def __generatePass(self, chars_list):
        result = []
        for _ in range(self.length):
            result.append(random.choice(chars_list))

        return ''.join(result)


    def getPass(self):
        if self.strong == 0:
            return self.__generatePass(self.__lower_letters + self.__upper_letters)
        elif self.strong == 1:
            return self.__generatePass(self.__lower_letters + self.__numbers + self.__upper_letters)
        else:
            return self.__generatePass(self.__lower_letters + self.__symbols + self.__upper_letters + self.__numbers)
    
    def __str__(self):
        return '{}'.format(self.getPass())
