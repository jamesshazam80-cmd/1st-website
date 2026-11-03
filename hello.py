import operator


OPERATIONS = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.truediv,
}


def calculator():
	print("Calculator (+, -, *, /). Enter q to quit.")

	while True:
		first_input = input("First number: ").strip()
		if first_input.lower() == "q":
			print("Goodbye!")
			break

		try:
			first_number = float(first_input)
			operation = input("Operation (+, -, *, /): ").strip()
			second_number = float(input("Second number: ").strip())

			if operation not in OPERATIONS:
				print("Please choose +, -, *, or /.")
				continue
			if operation == "/" and second_number == 0:
				print("Cannot divide by zero.")
				continue

			result = OPERATIONS[operation](first_number, second_number)
			print(f"Result: {result:g}")
		except ValueError:
			print("Please enter valid numbers.")


if __name__ == "__main__":
	calculator()
