def main():
	
	countries = ['USA', 'Poland']

	while True:
		try:		
			number = int(input('Insert your cellphone number in plain text: '))
			number = str(number)
			while len(number) > 15:		
				print('Your number is too long! Max 15 digits allowed.')
				main()
				break
			break
		except:
			print('Not a valid number')

	country = input('From what country are you from? ').lower()

	while True:
		if country == 'usa':
			

			if len(number) > 7:
				
				length = 7
				urlength = len(number)

				length = str(length)
				urlength = str(urlength)

				print('Error! US telephone number length is ' + length + '. Your number is ' + urlength + ' characters long.')
				print('')
				main()

			elif len(number) < 7:

				length = 7
				urlength = len(number)

				length = str(length)
				urlength = str(urlength)

				print('Error! US telephone number length is ' + length + '. Your number is ' + urlength + ' characters long.')
				print('')
				main()

			else:

				state = input('What is your area code? ') 

				usprt1 = number[0:3]
				usprt2 = number[3:7]

				number = usprt1 + '-' + usprt2

				number = str(number)
				number = '+1 ' + state +'-' + number
				
				print('')
				print('Your Cellphone number is: ' + number)

			break

		elif country == 'poland':
			
			if len(number) > 9:
				
				length = 9
				urlength = len(number)

				length = str(length)
				urlength = str(urlength)

				print('Error! Polish telephone number length is ' + length + '. Your number is ' + urlength + ' characters long.')
				print('')
				main()

			elif len(number) < 9:

				length = 9
				urlength = len(number)

				length = str(length)
				urlength = str(urlength)

				print('Error! Polish telephone number length is ' + length + '. Your number is ' + urlength + ' characters long.')
				print('')
				main()

			else:
				n = 3

				number = [number[i:i+n] for i in range(0, len(number), n)]
				number = ' '.join(number)
				number = str(number)
				number = '+48 ' + number
				
				print('')
				print('Your Cellphone number is: ' + number)

			break

		else:
			print('This country is currently unavaiable! Please try diffrent one!')
			print('Supported countries: ' + ', '.join(countries))
			country = input('From what country are you from? ').lower()


main()
print('')
input('Press ENTER to exit')