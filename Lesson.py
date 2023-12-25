print("Task 2")
number = int(input("Введіть тризначне число: "))

a = number // 100

b = number // 10 % 10

c = number % 10

print("Сотні",a)
print("Десятки",b)
print("Одиниці",c)
print("Сума",a + b + c)

print("Task 3")

a = input("Введіть першу цифру: ")
b = input("Введіть другу цифру: ")

print(a + b)