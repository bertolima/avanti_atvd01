#Luís André Bertoli dos Santos Lima
numberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
numberList2 = [3, 4, 5, 6, 9, 10, 11]
#questao 01
def getPrimes(lista):
    def isPrime(number):
        if (number == 0 or number == 1):
            return False
        for i in range(2, number):
            if(number % i == 0):
                return False
        return True
    
    primes = []
    for value in lista:
        if (isPrime(value)):
            primes.append(value)

    return primes

#questao02
def separateLists(v1,v2):
    ans = []
    for elem in v1:
        if (elem in v2):
            continue
        else:
            ans.append(elem)

    return ans

#questao 03
def getSecondMax(lista:list):
    aux = [x for x in lista]
    elem = max(aux)
    aux.remove(elem)
    ans = max(aux)
    return ans

