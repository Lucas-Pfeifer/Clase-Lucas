import random
import time

def generateWinnerNumbers(size, width):
    winners = list()
    while(len(winners) != size):  
        ball = random.randint(1,width)
        if not ball in winners:
            winners.append(ball)
    return winners


def WinnerTier():
    MiLoto = generateWinnerNumbers(15, 20)
    numeros_ganadores = generateWinnerNumbers(15, 20)
    print("Winner numbers are:", numeros_ganadores)
    aciertos = 0

    for ball in MiLoto:
        if ball in numeros_ganadores:
            aciertos += 1

    print(aciertos)
    if aciertos <= 8:
        print("Perdiste")
        return 0
    
    elif aciertos <= 12:
        print("Ganaste 50.000") 
        return 50000

    elif aciertos <=14:
        print("Ganaste 1.000.000")
        return  1000000
        
    elif aciertos == 15:        
        print("Chao Jefe (150.000.000)")
        return 150000000

    
#llamar funcion e imprimir "Gane XX! si es mas de 100000" o "Sad gane poco si es menos"
Loteria = WinnerTier()
if Loteria>= 1000000:
    print(f'Ganaste {Loteria}')
else:
    print("Sad gane muy poco")