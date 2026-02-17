from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor
import time

# def dormir(tempo):
#     time.sleep(tempo)
#     print(f'Aguardo de {tempo} segundos')
    
# lista = [5,4,1,9,4,7,5,1.5,1.2,2.5,6,3.4,5.4]

# inicio = time.time()
# with ThreadPoolExecutor() as executor:
#     executor.map(dormir, lista)
# fim = time.time()

# total = fim - inicio
# print(f'TEMPO TOTAL {total}')

# print(# * 50)

def dormir(tempo):
    time.sleep(tempo)
    print(f'Aguardo de {tempo} segundos')
    return tempo
    
numeros_originais = [5,4,1,9,4,7,5,1.5,1.2,2.5,6,3.4,5.4]

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        dicionario = {}
        
        inicio = time.time()
        
        for numero in numeros_originais:
            future = executor.submit(dormir, numero)
            dicionario[future] = numero
            
        for dado in as_completed(dicionario):
            dict_ = dicionario[dado]
            retorno = dado.result()
    
    fim = time.time()
    
    total = fim - inicio
    print(f'TEMPO TOTAL {total}')
