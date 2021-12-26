#Source: https://github.com/Isaaker/Munchkin-Assistant
import time
def charity():
    cards = input ("¿Cuantas cartas tiene?")
    if cards == ("5"):
        print ("Tu turno a finalizado")
    if cards <= ("5"):
        print ("Tu turno a finalizado")
    if cards >= ("5"):
        cards2 = input ("Tienes el nivel mas bajo? [s/n] ")
        if cards2 == ("s"):
            print ("Descarta el excedente ")
            print ("Tu turno a finalizado")
        if cards2 == ("n"):
            print ("Dale el excendente a el jugadores con menor nivel")
            print ("Tu turno a finalizado")
def combat():
    print (" ")
    print ("Compara el nivel total de todos los mounstruos con el total de tu nivel con bonus (si te estan ayudando añade a la operacion el nivel y bonus de la otra persona)")
    combat1 = input ("¿Te puedes defender del Mountruo? [s/n] ")
    if combat1 == ("s"):
        print ("Has conseguido matar al mounstruo, coge una carta dungeon bocaabajo (si te ayudaron lo deberas de hacer boca arriba)")
        charity()
    if combat1 == ("n"):
        combat2 = input ("¿Puedes huir? [s/n] ")
        if combat2 == ("s"):
            print ("Para huir tendras que tirar el dado")
            combat3 = input ("Si consigues 5 o mas de 5 pulsa [+] si consigues menos de 5 pulsa [-].")
            if combat3 == ("+"):
                print ("Has conseguido escapar !!")
                charity()
            if combat3 == ("-"):
                print ("Sufres el mal rollo o males rollos en el caso de que sean varios")
                charity()
        if combat2 == ("n"):
            print ("Pidele ayuda a otro jugador, solo puedes elejir una persona a si que piensalo bien")
            combat()
def loot():
    print ("Coge una carta Dungeon y guardala en tu mano o ponla en juego ahora")
    charity()
def findproblems():
    find1 = input ("¿Tienes alguna carta de mounstruo en tu mano? [s/n] ")
    if find1 == ("s"):
        combattomonster = input ("¿Quieres pelear con ese mounstruo? [s/n] ")
        if find1 == ("s"):
            print ("Juega la carta")
            combat()
        if find1 == ("n"):
            loot()
print ("    Munchkin-Assistant    ")
print ("     Version Española ")
print (" ")
print ("Created by: Isaac Hernán")
print ("Powered by: Python 3")
print ("Hosted  by: GitHub")
print ("License by: Creative Commons")
print ("")
print ("Inicializando...")
time.sleep(5)
print ("-----------")
while True:
    print ("Version clasica de Munchkin")
    print ("A. Continuar el juego")
    print ("B. Finalizar el juego")
    if loop == ("a"):
        print ("Coge una carta")
        time.sleep(5)
        ismonster = input ("¿Es un mounstruo? [s/n] ")
        if ismonster == ("s"):
            print ("Es un mounstruo")
            combat()
        if ismonster == ("n"):
            curse = input ("¿Es una maldicion? [s/n] ")
        if curse == ("s"):
            print ("La maldicon te afecta")
            findproblems()
        if curse ("n"):
            print ("Guarda la carta o ponla en juego ahora")
            findproblems()                
    if loop == ("b"):
        print ("Gracias por usar nuestro programa")
        time.sleep(5)
        exit()


