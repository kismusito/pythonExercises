import math

"""
Profe en este archivo van a estar todos los problemas propuestos, separando el problema por comentarios
pero todos van a estar dentro del archivo.
"""

print("1) Realizar la carga del lado de un cuadrado, mostrar por pantalla el perímetro del mismo \n (El perímetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)")

ladoC = float(input("Type one side of the square: "))
print("Perimeter: " + str(math.floor(ladoC*4)))


print("2) Escribir un programa en el cual se ingresen cuatro números, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto.")


def calculateNumbers(listNumbers):
    print("Sum: " + str(sum(listNumbers[0:2])))
    numbersToMul = 1
    for x in listNumbers[2:4]:
        numbersToMul *= x
    print("Multiply: " + str(numbersToMul))


numbersGet = []


def getNumber():
    global numbersGet
    x = 1
    while x < 5:
        nP = math.floor(float(input("Please type a number: ")))
        numbersGet.append(nP)
        x += 1
    return numbersGet


calculateNumbers(getNumber())

print("3) Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.")


def calculateAverage(numbers):
    sumOfNumbers = sum(numbers)
    print("The sum is: " + str(sumOfNumbers))
    print("The average is: " + str(sumOfNumbers / len(numbers)))


numbersAverage = []


def getNumbersAverage():
    global numbersAverage

    i = 1
    while i <= 4:
        numbersAverage.append(float(input("Type a number: ")))
        i += 1
    return numbersAverage


calculateAverage(getNumbersAverage())


print("4) Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora.")


def calculateSalary(workerInfo):
    totalSalary = workerInfo['hours'] * workerInfo['valuePerHour']
    print(math.floor(totalSalary))


def workerInfo():
    infoWorker = {
        "hours": 0,
        "valuePerHour": 0
    }
    infoWorker["hours"] = float(input("How many hours you works: "))
    infoWorker["valuePerHour"] = float(input("What is the value per hour: "))

    return infoWorker


calculateSalary(workerInfo())


print("5) Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.")


def responseFive(numbers):
    if(numbers[0] > numbers[1]):
        totalSum = sum(numbers)
        totalDif = numbers[0] - numbers[1]
        print("The sum is: " + str(totalSum))
        print("The dif is: " + str(totalDif))
    elif(numbers[0] < numbers[1]):
        totalProd = numbers[0] * numbers[1]
        totalDivi = 0
        if(numbers[1] > 0):
            totalDivi = numbers[0] / numbers[1]
        else:
            print("The number 2 can't be 0")

        print("The product is: " + str(totalProd))
        print("The division is: " + str(totalDivi))


totalNumbers = []


def typeNumbers():
    global totalNumbers
    x = 1
    while x <= 2:
        totalNumbers.append(float(input("Type the number " + str(x) + ": ")))
        x += 1
    return totalNumbers


responseFive(typeNumbers())


print("6) Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje &quot;Promocionado&quot;.")


def responseSix(notes):
    lenNotes = len(notes)
    totalNote = sum(notes)
    totalAverage = math.floor(totalNote / lenNotes)
    if(totalAverage >= 7):
        print("Approved")
    else:
        print("Reject")


totalNotes = []


def getNumbersSix():
    global totalNotes
    x = 1
    while x <= 3:
        totalNotes.append(float(input("Type note " + str(x) + " : ")))
        x += 1

    return totalNotes


responseSix(getNumbersSix())


print("7) Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos. \n (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)")

def evaluateNumber(number):
    if(number < 0):
        print("the number is negative")
    else:
        numberFormat = str(number).split('.')
        print("The number has " + str(len(str(numberFormat[0]))) + " digits and " + str(
            len(str(numberFormat[1]))) + " decimals")

evaluateNumber(float(input("Number: ")))

print("8) Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.")

def getTheHight(numbers):
    print("The highest number is: " + str(max(numbers)))
    
inputNumbers = []
def inputNumbersEight():
    global inputNumbers
    x = 1
    while x <= 3:
        inputNumbers.append(float(input("Type the number " + str(x) + " : " )))
        x += 1
    
    return inputNumbers

getTheHight(inputNumbersEight())


print("9) Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)")

def responseNine(number):
    if(number >= 1):
        print("The number is positive")
    elif(number < 0):
        print("The number is negative")
    else:
        print("The number is 0")

responseNine(int(input("Type a entire number: ")))


print("10) Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.")

def responseTen(number):
    decodeNumber = str(number).split('.')
    if(len(decodeNumber[0]) <= 3 and len(decodeNumber[0]) >= 1):
        print("The number has " + str(len(decodeNumber[0])) + " digits and " + str(len(decodeNumber[1])) + " decimals")
    else:
        print("The number only must containt 3 digits")

responseTen(float(input("Type a number: ")))


print("11) Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:")

def responseEleven(aspirant):
    threeRule = (int(aspirant.get('correctQuestions')) * 100) / int(aspirant.get('numberOfQuestions'))
    if(threeRule >= 90):
        print("Maximun")
    elif(threeRule >= 75 and threeRule < 90):
        print("Medium")
    elif(threeRule >= 50 and threeRule < 75):
        print("Regular")
    else:
        print("No calificate")

def aspirantInfo():
    aspirant = {
        "numberOfQuestions": 0,
        "correctQuestions": 0
    }

    aspirant['numberOfQuestions'] = int(input("Number of questions: "))
    aspirant['correctQuestions'] = int(input("Number of correct questions: "))

    return aspirant

responseEleven(aspirantInfo())


print("12) Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad. day/month/year")

monthsOfYear = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "June",
    "6": "July",
    "7": "August",
    "8": "September",
    "9": "October",
    "10": "November",
    "12": "It's chrismast"
}

def responseTwelve(date):
    global monthsOfYear
    dateGet = date.split('/')
    if(monthsOfYear.get(dateGet[1])):
        print(monthsOfYear.get(dateGet[1]))
    else:
        print("Date invalid")

responseTwelve(input("Date day/month/year: "))

print("13) Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero.")


def responseThirteen(numbers):
    isEqual = False
    oneBig = False
    for i in range(len(numbers)):
        if i+1 == len(numbers):
            if(numbers[i] == numbers[i-1]):
                isEqual = True
            else:
                oneBig = True
        else:
            if(numbers[i] == numbers[i+1]):
                isEqual = True
            else:
                oneBig = True

    if(isEqual and oneBig == False):
        sumNumbers = sum(numbers[0:2])
        productNumber = sumNumbers * numbers[-1]
        print("The sum is: " + str(sumNumbers))
        print("The product is: " + str(productNumber))
    else:
        print("One number is not equal")


numbersThirteen = []


def getNumbersThirteen():
    global numbersThirteen
    x = 1
    while x <= 3:
        numbersThirteen.append(float(input("Number " + str(x) + " : ")))
        x += 1
    return numbersThirteen


responseThirteen(getNumbersThirteen())


print("14) Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda &quot;Todos los números son menores a diez&quot;.")

def responseFourteen(numbers):
    isLowerTeen = False
    isOneHight = False
    for i in numbersFourteen:
        if i < 10:
            isLowerTeen = True
        else:
            isOneHight = True
            break
    
    if(isLowerTeen and isOneHight == False):
        print("Todos los números son menores a diez")
    else:
        print("There are one number hight than 10")

numbersFourteen = []
def getNumbersFourteen():
    global numbersFourteen
    x = 1
    while x <= 3:
        numbersFourteen.append(float(input("Number " + str(x) + " : ")))
        x +=1
    return numbersFourteen

responseFourteen(getNumbersFourteen())

print("15) Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda &quot;Alguno de los números es menor a diez&quot;.")

def responseFiveteen(numbers):
    isOneBig = False
    for i in numbers:
        if i < 10:
            isOneBig = True

    if isOneBig:
        print("Alguno de los números es menor a diez")
    else:
        print("No number is less than 10")



numbersFiveteen = []
def getNumbersFiveteen():
    global numbersFiveteen
    x = 1
    while x <= 3:
        numbersFiveteen.append(float(input("Number " + str(x) + " : ")))
        x +=1
    return numbersFiveteen

responseFiveteen(getNumbersFiveteen())


print("16) Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. \n (1º Cuadrante si x &gt; 0 Y y &gt; 0 , \n 2º Cuadrante: x &lt; 0 Y y &gt; 0, etc.)")

def responseSixteen(numbers):
    if ( numbers[0] > 0 and numbers[1] > 0):
        print("Cuadrant 1")
    elif ( numbers[0] < 0 and numbers[1] > 0):
        print("Cuadrant 2")

numbersSixteen = []
def getNumbersSixteen():
    global numbersSixteen
    x = 1
    while x <= 2:
        numbersSixteen.append(float(input("Number " + str(x) + " : ")))
        x +=1
    return numbersSixteen

responseSixteen(getNumbersSixteen())


print("17) De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe: \n a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar. \n b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %. \n c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.")

def calculeSeventeen(worker):
    if ( worker.get("salary") < 500 and worker.get("yearsOld") >= 10):
        newSalary = worker.get("salary") * .2
        worker['salary'] = worker.get('salary') + newSalary
    elif (worker.get("salary") < 500 and worker.get("yearsOld") < 10):
        newSalary = worker.get("salary") * .05
        worker['salary'] = worker.get('salary') + newSalary

    print("Worker salary: " + str(worker.get('salary')))

def getWorkerSeventeen():
    worker = {
        "salary": 0,
        "yearsOld": 0
    }

    worker["salary"] = float(input("Your salary: "))
    worker["yearsOld"] = float(input("Antiquity: "))

    return worker

calculeSeventeen(getWorkerSeventeen())


print("18) Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)")

def responseEighteen(numbers):
    minNumberEighteen = min(numbers)
    maxNumberEighteen = max(numbers)
    diferenceBetweenEighteen = maxNumberEighteen - minNumberEighteen
    print("Min number: " + str(minNumberEighteen))
    print("Max number: " + str(maxNumberEighteen))
    print("Diference: " + str(diferenceBetweenEighteen))

numbersEighteen = []
def getNumbersEighteen():
    global numbersEighteen
    x = 1
    while x <= 3:
        numbersEighteen.append(float(input("Number " + str(x) + " : ")))
        x +=1
    return numbersEighteen

responseEighteen(getNumbersEighteen())

print("19) Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.")

def evalueNotesNineteen(notes):
    moreSeven = 0
    lessSeven = 0
    for i in notes:
        if i >= 7:
            moreSeven += 1
        elif (i < 7 and i >= 1):
            lessSeven += 1
        
    print("Hight than 7: " + str(moreSeven))
    print("Less than 7: " + str(lessSeven))

numbersNineteen = []
def getNumbersNineteen():
    global numbersNineteen
    x = 1
    while x <= 10:
        numbersNineteen.append(float(input("Number " + str(x) + " : ")))
        x +=1
    return numbersNineteen

evalueNotesNineteen(getNumbersNineteen())

print("20) Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas. in meters")

def evalueheightsTwelve(heights):
    totalSumHeights = sum(heights)
    totalHeights = len(heights)
    print(round((totalSumHeights / totalHeights) , 2))


heightsTwelve = []
def getheightsTwelve():
    global heightsTwelve
    x = 1
    numberOfHeights = int(input("Number of heights: "))
    while x <= numberOfHeights:
        heightsTwelve.append(float(input("Height " + str(x) + " : ")))
        x +=1
    return heightsTwelve

evalueheightsTwelve(getheightsTwelve())


print("21) En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.")

def responseTwentyOne(workers):
    totalSalary = []
    salaryBetween100And300 = 0
    salaryMore300 = 0
    for i in workers:
        salaryC = i.get('salary')
        totalSalary.append(salaryC)
        if (salaryC >= 100 and salaryC < 300):
            salaryBetween100And300 += 1
        elif salaryC >= 300:
            salaryMore300 += 1
    
    print("Between 100 and 300: " + str(salaryBetween100And300))
    print("More than 300: " + str(salaryMore300))

workersTwentyOne = []
def getNumberOfWorkersTwentyOne():
    global workersTwentyOne
    x = 1
    numberOfWorkersTwentyOne = int(input("Number of workers: "))
    while x <= numberOfWorkersTwentyOne:
        newWorker = {
            "salary": 0
        }
        newWorker['salary'] = float(input("Salary of Worker " + str(x) + " : "))
        workersTwentyOne.append(newWorker)
        x +=1
    return workersTwentyOne

responseTwentyOne(getNumberOfWorkersTwentyOne())


print("22) Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)")

def printSerie(serie):
    for i in serie:
        print(i)

def serie(number , totalCounter):
    listSerie = []
    numberToSerie = number
    prevNumber = numberToSerie
    x = 1
    while x <= totalCounter:
        listSerie.append(prevNumber)
        prevNumber = numberToSerie + prevNumber
        x += 1

    return listSerie

printSerie(serie(11 , 25))


print("23) Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24,etc.")

def printMulti(listMul):
    for i in listMul:
        print(i)

def multiplyOfNumber(number):
    continueSerie = True
    mul = 1
    listOfMul = []
    while continueSerie:
        numberMul = number * mul
        if(numberMul >= 500):
            continueSerie = False
            continue
        listOfMul.append(numberMul)
        mul += 1
    return listOfMul

printMulti(multiplyOfNumber(int(input("Number: "))))


print("24) Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes &quot;Lista 1 mayor&quot;, &quot;Lista 2 mayor&quot;, &quot;Listas iguales&quot;) Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.")

def responseTwelveFour(listGet):
    listOne = sum(listGet[0])
    listTwo = sum(listGet[1])
    
    if listOne == listTwo:
        print("Listas iguales")
        print("List 1: " + str(listOne) + " List 2: " + str(listTwo))
    elif listOne > listTwo:
        print("Lista 1 mayor")
        print("List 1: " + str(listOne) + " List 2: " + str(listTwo))
    else:
        print("Lista 2 mayor")
        print("List 1: " + str(listOne) + " List 2: " + str(listTwo))

def getLists():
    generalList = []
    for i in range(2):
        listContainer = []
        for j in range(5):
            listContainer.append(float(input("Number to list " + str(i+1) + " : ")))
        generalList.append(listContainer)
    
    return generalList

responseTwelveFour(getLists())


print("25) Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares. Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):")

def responseTwelveFive(numbers):
    nPar = 0
    nInpar = 0
    for i in numbers:
        if i % 2 == 0:
            nPar += 1
        else:
            nInpar += 1
    
    print("Par numbers: " + str(nPar))
    print("Inpar numbers: " + str(nInpar))


def uploadNumbersTwelvefive():
    listOfNumbers = []
    totalNumbers = int(input("How many numbers: "))
    x = 1
    while x <= totalNumbers:
        listOfNumbers.append(int(input("Number " + str(x) + " : ")))
        x += 1
    return listOfNumbers

responseTwelveFive(uploadNumbersTwelvefive())


print("26) Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar: a) De cada triángulo la medida de su base, su altura y su superficie. b) La cantidad de triángulos cuya superficie es mayor a 12.")

def getArea(triangleInfo):
    area = (triangleInfo.get('base') * triangleInfo.get('altura')) / 2
    triangleInfo['area'] = area
    return triangleInfo

def responseTwelveSix(triangles):
    totalTriangles = []
    for i in triangles:
        newTriangle = getArea(i)
        totalTriangles.append(newTriangle)
    return totalTriangles

def printTriangles(triangles):
    moreThan12 = 0
    for i in triangles:
        print(i)
        if(i.get('area') > 12):
            moreThan12 += 1
        
    print("More than 12: " + str(moreThan12))


def trianglesList():
    listOfTriangles = []
    totalTriangles = int(input("How many triangles: "))
    x = 1
    while x <= totalTriangles:
        triangleInfo = {
            "base": 0,
            "altura": 0,
            "area": 0
        }
        print("Triangle " + str(x))
        triangleInfo['base'] = float(input("Base: "))
        triangleInfo['altura'] = float(input("Altura: "))
        listOfTriangles.append(triangleInfo)
        x += 1
    return listOfTriangles

printTriangles(responseTwelveSix(trianglesList()))


print("27) Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.")

def printNumbersTwelveSeven(numbers):
    numbers.reverse()
    sumNumbers = 0
    print(numbers)
    if(len(numbers) >= 5):
        for i in range(5):
            sumNumbers += numbers[i]
    else:
        sumNumbers = sum(numbers)
    print("Sum: " + str(sumNumbers))

def getValuesTwelveSeven():
    listOfNumbers = []
    totalNumbers = int(input("Total numbers: "))
    x = 1
    while x <= totalNumbers:
        listOfNumbers.append(float(input("Number " + str(x) + " : ")))
        x += 1
    return listOfNumbers

printNumbersTwelveSeven(getValuesTwelveSeven())


print("Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)")

def printMultiplyTable(number , index):
    for i in range(1, index+1):
        actualResult = number * i
        print(str(number) + " x " + str(i) + " = " + str(actualResult))

printMultiplyTable(5 , 10)


print("28) Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos) Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.")

def printTalbe(number):
    if number:  
        for i in range(1, 12+1):
            print(str(number) + " x " + str(i) + " = " + str((number*i)))

def getNumber():
    numberTo = int(input("Number 1 to 10: "))
    if (numberTo <= 10 and numberTo >= 1):
        return numberTo
    else: 
        print("Only numbers from 1 to 10")
        return False
    
printTalbe(getNumber())

print("Realizar un programa que lea los lados de n triángulos, e informar: a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual) b) Cantidad de triángulos de cada tipo.")