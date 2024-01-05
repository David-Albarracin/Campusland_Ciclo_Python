import os
import controllers.clientes as clientServices
import templates.menus as menus

def suma(**kwargs):
    print(kwargs)

if __name__ == "__main__":
   
    di = {'a': {"10":10}, 'b':20}
    suma(**di) # 30
    os.system("pause")
    while(True):
        os.system("cls")
        opMenu = input(menus.printMenus(menus.header, menus.opcions))
        if(opMenu == "1"):
            clientServices.menu()
        elif(opMenu == "2"):
            pass
        elif(opMenu == "3"):
            pass
        elif(opMenu == "4"):
            break
        else:
            print(menus.valueErrorMessage)

        os.system("pause")