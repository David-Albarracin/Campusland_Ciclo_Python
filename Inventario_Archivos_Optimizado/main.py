import os
import controllers.clientes as clientServices
import templates.menus as menus


if __name__ == "__main__":
    while(True):
        opMenu = input(menus.printMenus("main"))
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