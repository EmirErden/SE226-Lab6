user_input = int(input("Please enter a number for calculate: "))
total_numbers = []
a = 1
calculator = lambda x: (x-3)/x ** 2

while a <= user_input:
    total_numbers.append(calculator(a))
    a = a+1

total = sum(total_numbers)
print(total)

user_input2 = int(input("Please enter a number for the second calculation: "))


def capital_pi(number):
    initial_number: int = 1
    total2: float = 1

    def calculator2(ex_number):
        return (ex_number/(ex_number+2))-10

    while initial_number <= number:
        total2 = total2 * calculator2(initial_number)
        initial_number = initial_number + 1

    print(total2)


capital_pi(user_input2)
