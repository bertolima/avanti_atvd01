#Luís André Bertoli dos Santos Lima

#questao 01
def getPrimes(lista):
    def isPrime(number):
        if (number == 0 or number == 1):
            return False
        for i in range(2, int(number ** 0.5) + 1):
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

#questao 04
def sortTupleList(lista:list[tuple[str,int]]):
    lista.sort()

#questao 05
#R- Devemos iniciar primeiramente a variavel min_num = MAX_INT e a varivael max_num = -MAX_INT,
#assim, só devemos percorrer a lista e pra cada iteração fazemos dois ifs, um deles seria pra
#checar se algum numero é maior que min_num, se sim, min_num recebe o valor desse número e
#fazer o contrário para max_num. Dessa forma, ao final da iteração teremos o maior valor da
#lista em max_num e o menor valor da lista em min_num, função que faz isso:

def minAndMax(lista):
    min_num = float('inf')
    max_num = float('-inf')
    for value in lista:
        if (value < min_num): min_num = value
        if (value > max_num): max_num = value
    return min_num, max_num

#questao 06
#R- Para ler um arquivo csv podemos utilizar o método "read_csv" do pandas, então teremos:
#dataframe = pd.read_csv("diretorio do .csv"). Para exibir as primeiras linhas podemos
#usar o método "head" do pandas, nesse caso: dataframe.head(número de linhas).

#questao 07
#R- Para filtrar as linhas de uma coluna espécica de um dataframe com base em uma condição
#podemos utilizar a notação dataframe["coluna selecionada"] condição. Por exemplo:
#pessoas["idade"] > 18. Iremos filtrar o dataframe pessoas em quais linhas a coluna "idade" assume valores
#maiores que 18.

#questao 08
#R- Primeiros devemos verificar se existem valores NaN no dataframe, para isso, podemos
#usar o método "isnan", então: valores_nan = dataframe.isnan(). Para tratar esses valores
#podemos preencher esse valores com valores escolhidos com dataframe.fillna(valor, inplace=True)
#ou podemos simplesmente remover esses valores com dataframe.dropna(inplace=True).

#questao 09
import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
layout="constrained")
for row in range(2):
  for col in range(2):
      axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                            transform=axs[row, col].transAxes,
                            ha='center', va='center', size=18,
                            color='darkgrey') 
fig.suptitle('plt.subplots()')


#questao 10
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x,y)







