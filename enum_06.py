# Função enumerate
l1 = ["eat", "sleep", "repeat"]
s1 = "Geek"
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type: ", type(obj1))
print("Return type: ", type(obj2))
print(list(enumerate(l1)))
print(list(enumerate(s1, 2)))