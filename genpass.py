import random

# strong (0, 1, 2)
def genpass(length, strong=2):
    numbers = [chr(x) for x in range(48, 58)]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    lower_letters = [chr(x) for x in range(97, 123)]
    upper_letters = [chr(x) for x in range(65, 91)]

    def randompass(length, chars_list):
        result = []
        for _ in range(length):
            result.append(random.choice(chars_list))

        return ''.join(result)
    
    if strong == 0:
        return randompass(length, lower_letters + upper_letters)
    elif strong == 1:
        return randompass(length, lower_letters + numbers + upper_letters)
    else:
        return randompass(length, lower_letters + symbols + upper_letters + numbers)

for i in range(10):
    print(genpass(16))