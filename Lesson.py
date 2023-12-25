number = int(input("Введіть тризначне число: "))

a = number // 100

b = number // 10 % 10

c = number % 10

print("Сотні",a)
print("Десятки",b)
print("Одиниці",c)
print("Сума",a + b + c)