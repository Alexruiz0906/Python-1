import os
casa= ["sala", "comedor", "cocina", "baño", "recamara"]
name = "felipe"
while True:
    llega = input("LLega a casa?: Y/N: ").upper()
    if llega == "Y":
        print(name + " llega a casa")
        os.system("clear")
        print( name + " Deja el termo y el bolso en la " + casa[0])
        print(name + " va al " + casa[3] + " a darse una ducha")
        while True:
            bath= input("Se dio una ducha?: Y/N: ").upper()
            if bath == "Y":
                os.system("clear")
                print(name + " se dio una ducha y se dirige a la " + casa[4] + " a vestirse")
                break
            else:
                os.system("clear")
                print(name + " no ha terminado de bañarse")
        while True:
            clothes = input(name + " ya se vistio?: Y/N: ").upper()
            if clothes == "Y":
                os.system("clear")
                print(name + " ya se vistio y se dirige a la " + casa[2] + " a ver que hay de comer")
                break
            else:
                os.system("clear")
                print(name + " no se ha vestido")
                
        while True:
            eat = input("habia algo  liviano ya hecho?: Y/N: ").upper()
            if eat == "Y":
                os.system("clear")
                print(name + " come algo y se dirige a la " + casa[4] + " para dormir")
                break
            else :
                os.system("clear")
                print(name + " no habia nada hecho y cocina algo liviano")
        while True:
            light = input("la luz de la " + casa[4] + " esta encendida?: Y/N: ").upper()
            if light == "Y":
                os.system("clear")
                print(name + " apaga la luz y se acuesta a dormir")
                break
            else:
                os.system("clear")
                print(name + " se acuesta a dormir")
                break
        break
    else:
        print(name + " aun no ha llegado a casa")



