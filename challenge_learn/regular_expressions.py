import re

texto = "O usuário logado é o admin_01 com acesso root."

# Padrão: "admin_" seguido de dígitos (\d+)
padrao = r"admin_\d+"

result = re.search(padrao, texto)

if result:
    print(f"Encontrado: {result.group()}") # .group() extrai o texto achado
else:
    print("Não encontrado.")


# Challenge

mils = float(input('Enter a distance in miles: '))

covert_mils_to_km = mils * 1.609344

print(f'Mils: "{mils}", if mils converted to km: {covert_mils_to_km:.3f}')
