user_input = int(input("Please enter a number for calculate: "))
total_numbers = []
a = 1
calculator = lambda x: (x-3)/x ** 2

while a <= user_input:
    total_numbers.append(calculator(a))
    a = a+1

total = sum(total_numbers)
print(total)

# Question 2

user_input2 = float(input("Please enter a number for the second calculation: "))

product = 1


def capital_pi(number):
    """This function calculates product of (number/(number+2))-10 till the nuber is zero"""

    global product
    if number >= 1:
        product = (number/(number+2))-10 * capital_pi(number-1)
    return product


capital_pi(user_input2)
