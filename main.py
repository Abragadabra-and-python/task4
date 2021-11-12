from math import sqrt, factorial


def abragadabra(a, b):
	numbers = [sqrt(factorial(i)) for i in range(a, b) if i % 2 == 0]

