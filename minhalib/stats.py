import math

def mean(x):
     total = 0
     for i in x:
         total += i
     return total / len(x)

def stdev(x):
	return math.sqrt(var(x))

def var(y):
	media = mean(y)
	soma = 0
	variancia = 0

	for valor in y:
		soma += math.pow((valor-media), 2)
	variancia = soma / float(len(y)) 
	return variancia
