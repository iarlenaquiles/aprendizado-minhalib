import math
import numpy as np 

def split_train_test(n_elem, perc_train, seed):
	numero_elementos = [i for i in range(n_elem)]
	elementos_treinamento = math.floor(perc_train * n_elem)
	np.random.seed(seed)
	np.random.shuffle(numero_elementos)
	treino = numero_elementos[0:elementos_treinamento]
	teste = numero_elementos[elementos_treinamento:]
	return treino, teste
