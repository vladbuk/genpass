import random
from genpass_class import Genpass

class Check_Genpass(Genpass):
    random.seed(0)

pass1 = Check_Genpass(8)
pass2 = Check_Genpass(16, 0)
pass3 = Check_Genpass(12, 1)
pass4 = Check_Genpass(1, 2)

def test_genpass_class():
    """ Test generating password with specific length and strong """
    assert pass1.getPass() == 'LPf*1YNA'
    assert pass2.getPass() == 'EwLnGisiWgNZqITZ'
    assert pass3.getPass() == 'CVjtgKeVSHv4'
    assert pass4.getPass() == '7'
    print('Base password generatind test')

# print(pass1.getPass())
# print(pass2.getPass())
# print(pass3.getPass())
# print(pass4.getPass())