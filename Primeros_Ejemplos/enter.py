import os 

isActived = True


while isActived:
    rst = input("Continuar si(n) Enter(no).. ")
    if (rst in "Ss"):
        print("p")
        isActived = bool(rst)
    else:
        pass
