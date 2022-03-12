def add(num1, num2):
	return num1 + num2


def subtract(num1, num2):
	return num1 - num2


def divide(num1, num2):
	return num1 / num2


def mult(num1, num2):
	return num1 * num2


print("Please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Multiply\n" \
      "4. Divide\n")

# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
number_1, number_2 = int(input()), int(input())

if select == 1:
	print(number_1, "+", number_2, "=",
	      add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
	      subtract(number_1, number_2))
elif select == 3:
	print(number_1, "/", number_2, "=",
	      divide(number_1, number_2))
elif select == 3:
	print(number_1, "*", number_2, "=",
	      mult(number_1, number_2))
