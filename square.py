from random import randint
square_numbers = []

for number in range(1, 1000):
	square_numbers.append(number ** 2)

problem = (square_numbers[randint(1,len(square_numbers))] * square_numbers[randint(1,len(square_numbers))])

print('The randomly selected number is (two square numbers multiplied) - ' + str(problem))

for x in range(1, len(square_numbers)):
	
	if (problem / square_numbers[x]) in square_numbers:
		print(str(square_numbers[x]) + " x " + str(int(problem / square_numbers[x])) + ' equals ' + str(problem))
		square_numbers[x] = None
