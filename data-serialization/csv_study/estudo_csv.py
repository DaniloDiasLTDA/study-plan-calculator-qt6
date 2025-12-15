import csv

from pathlib import Path

ROOT_PATH = 'csv_study/'

FILE_CSV = ROOT_PATH + 'info_client.csv'

CLIENT_INFO = [
   {'client_name':'Danilo','client_invoice': 250 ,'paynotpay': 'pay'},
   {'client_name':'Maria','client_invoice': 660 ,'paynotpay': 'not'},
   {'client_name':'Jose','client_invoice': 350 ,'paynotpay': 'pay'},
   {'client_name':'Veneza','client_invoice': 79.90 ,'paynotpay': 'not'},
   {'client_name':'Saulo','client_invoice': 120.50 ,'paynotpay': 'pay'},
   {'client_name':'Carlos','client_invoice': 522.99 ,'paynotpay': 'not'},
   {'client_name':'Mauro','client_invoice': 3698.99, }
]


class MeuErro(TypeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print('Error Customizado')


with open(FILE_CSV, 'w', newline='', encoding='utf-8') as file_csv:
    """ Cria e abre o arquivo file_name.csv em modo de escrita 'w'
        'newline='' evita linhas em branco
        ecoding='utf-8 codifica corretamente os caracters
    """
    field_names = ['client_name','client_invoice', 'paynotpay'] # Criando as chaves da lista
    writing = csv.DictWriter(file_csv, fieldnames=field_names) #DictWriter cria um objeto e mapeia dicionarios em linhas

    writing.writeheader()
    writing.writerows(CLIENT_INFO)

# TODO: how create Enum - Secundário
# TODO: Create return Typex - Secundário

# TODO: Função para melhorar e dimuir o código
def read_file(file_name: str,mode: str = 'r'):
    with open(file_name,mode, newline='', encoding='utf-8') as file:
        return csv.DictReader(file)


def search_client(file_csv: str,search_name):    
    try:
        # Simplificar o código usando read_file 40 - 41
        with open(file_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file) 
            for client in reader:
                if 'client_name' in client and client['client_name'] == search_name:
                    return {'Nome': client['client_name'],
                                'Invoice': client['client_invoice'],
                                'Status': client['paynotpay']}
        
    except FileNotFoundError:
        print(f'Arquivo {file_csv} não encontrado')

    except TypeError:
        print(f'Nome do arquivo está incorreto {type(file_csv)}')
    
    except Exception:
        return MeuErro()

# TODO: Elaborar uma forma de procurar o status direto do arquivo .csv
def client_status(list_clients, search_name):
    for client in list_clients:
            if 'client_name' in client and client['client_name'] == search_name:
                if 'paynotpay' in client:
                    return {'name': client['client_name'], 'status': client['paynotpay']}
                else:
                    print(f"Aviso: Cliente '{search_name}' encontrado, mas a chave 'paynotpay' não existe.")
                    return {'name': client['client_name'], 'status': 'Informação de status ausente'}

    return f'Nenhum cliente encontrado com o nome exato "{search_name}".'

arquivo = ROOT_PATH + 'info_client.csv'

forc_error = None

result1 = search_client(arquivo, 'Danilo') # Chama a função corretamente
print(result1)

# TODO: Criar teste de unidade (PYTEST)
result2 = search_client(forc_error, 'Maria') #type: ignore
print(result2)

# TODO: Para cada linha desse CSV que estou enviando, quero para cada linha seja
# enviada para API de pagamento, só enviar o nome se pagou ou não / bool 
# * Usar uma API de testes
# * Requisitos: Visto que é uma requesição - Assync IO Python  

# TODO: async def payments_api.post_client_invoice_status(name, pay_not_pay)
