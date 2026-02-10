tools = ["Martelo", "machado", "Chave de fenda", "Parafusadeira"]


for item in tools:
    if item.upper().startswith("M"):
        print(f'{item} começa com "M"')
    else:
        print(f'{item} Não começa com "M"')
