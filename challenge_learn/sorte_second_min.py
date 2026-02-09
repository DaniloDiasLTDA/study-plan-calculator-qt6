import heapq

def find_second_smallest(lst):
    # Set remove duplicatas, sorted ordena, [1] pega o segundo elemento
    unique_elements = sorted(set(lst))
    return unique_elements[1] if len(unique_elements) > 1 else Non

# def find_second_smallest(lst):
#     # nsmallest(2, ...) retorna os dois menores elementos
#     unique_lst = list(set(lst))
#     two_smallest = heapq.nsmallest(2, unique_lst)
#     return two_smallest[1] if len(two_smallest) > 1 else None

lista = [ 1, 1, 3, 4, 6]

print(find_second_smallest(lista))