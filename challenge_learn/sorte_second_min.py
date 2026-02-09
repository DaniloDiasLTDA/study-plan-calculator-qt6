

def find_second_smallest(lst):
    # Set remove duplicatas, sorted ordena, [1] pega o segundo elemento
    unique_elements = sorted(set(lst))
    return unique_elements[1] if len(unique_elements) > 1 else Non


lista = [1, 1, 3, 4, 6]

print(find_second_smallest(lista))
