#import Audience

def set_modulus(list_elements):
    branche = input("branche: TC , 2IA , IF ")
    semester = int(input("ina semster:"))
    modulus = input('module')
    element = input('element')
    list_elements.append(element)
    if branche == 'TC':
        TC = ['GL','eMBI', 'IeL','ISEM','IWIM','SSI']
        for bra in TC:
            #!obj = Audience(branche=bra , semester = 'S%d'%semester , modulus = modulus , element = element)
            #!obj.save()
            pass
    else:
        #!obj = Audience(branche=bra , semester = 'S%d'%semester , modulus = modulus , element = element)
        #!obj.save()
        pass
if __name__=='__main__':
    list_elements = []
    while True:
        try:
            set_modulus(list_elements)
        except KeyboardInterrupt:
            print(list_elements)
            print("goodbye!")
