import csv

# from csv import _reader
from pathlib import Path

client_info = [
    ['Name','Value_invoice','PayNotPay'],
    ['Danilo', 200.50, 'NotPay'],
    ['Italo', 80.99, 'Pay'],
    ['Maria', 1240.30, 'NotPay'],
    ['Carlos', 22200, 'Pay'],
]

file_name = 'info_payment.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file_csv:
    """ Cria e abre o arquivo file_name.csv em modo de escrita 'w'
        'newline='' evita linhas em branco
        ecoding='utf-8 codifica corretamente os caracters
    """
    new_file = csv.writer(file_csv) # cria um objeto CSV
    new_file.writerows(client_info) # Escreve os dados no arquivo .CSV

# criar uma função que lê(open) ou escreve / melhorando o código

# TODO: how create Enum 
# TODO: Create return Type
def read_file(file_name: str,mode: str = 'r'):
    with open(file_name,mode, newline='', encoding='utf-8') as file:
        yield csv.reader(file)

def search_client(file_name,key,search_value):
        with read_file(file_name) as file:
            print(type(line))
            print([l for l in line])
            # if len(line) > key and line[key] == search_value:
            #     return f'{line}'
        return None


# def client_stats(file_name, search_key, search_value):
#         for line in read_file(file_name):
#             if len(line) > search_key and line[search_key] == search_value:
#                 if line[2] == 'NotPay':
#                    return f'Cliente {line[0]} está com o status: NotPay'
#                 else:
#                    return f'Cliente {line[0]} está dia.'


# TODO: Para cada linha desse CSV que estou enviando, quero para cada linha seja
# enviada para API de pagamento, só enviar o nome se pagou ou não / bool 
# * Usar uma API de testes
# * Requisitos: Visto que é uma requesição - Assync IO Python  

keySearch = 0

find_value1 = 'Maria'
resultS1 = search_client(file_name, keySearch, find_value1)
print(resultS1)
# resultC1 = client_stats(file_name, keySearch, find_value1)
# print(resultC1)

# find_value2 = 'Italo'
# resultS2 = search_client(file_name, keySearch, find_value2)
# print(resultS2)
# resultC2 = client_stats(file_name, keySearch, find_value2)
# print(resultC2)

