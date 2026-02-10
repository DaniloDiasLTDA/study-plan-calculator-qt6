# Método rápido
def has_unique_char(char):
    return len(set(char)) == len(char)


# Método Técnico
def has_unique_characters(sa):
    vistos = set()
    for char in sa:
        if char in vistos:
            return False
        vistos.add(char)
    return True


word1 = ("apple", "apple", "apple", "banana", "cherry")

word2 = "sample"

print(has_unique_char(word1))

print(has_unique_characters(word2))
