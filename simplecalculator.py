print('Simple calculator by Timur Yun (BMC202132729)') #prints title of the program
while True: #make loop so program don't exit after showing a result to user
	first_number = float(input('Please enter first number: ')) #asking user for first number
	second_number = float(input('Please enter second number: ')) #asking user for second number
	mathematical_action_that_user_wants_to_take = input('Please enter a mathematical action that you want to do +,-,*,/: ') #asking user for mathematical action
	if mathematical_action_that_user_wants_to_take == '+' or mathematical_action_that_user_wants_to_take == '-' or mathematical_action_that_user_wants_to_take == '*' or mathematical_action_that_user_wants_to_take == '/': #checking if value of mathematical_action_that_user_wants_to_take is + or - or / or *
		if mathematical_action_that_user_wants_to_take == '+': #code that will be executed if value of mathematical_action_that_user_wants_to_take is '+'
			print(first_number + second_number) #output to the display result of adding first_number with second_number
		elif mathematical_action_that_user_wants_to_take == '-': #code that will be executed if value of mathematical_action_that_user_wants_to_take is '-'
			print(first_number - second_number) #output the result of taking away second_number from first_number
		elif mathematical_action_that_user_wants_to_take == '*': #code that will be executed if value of mathematical_action_that_user_wants_to_take is '*'
			print(first_number * second_number) #output the result of multiply first_number by second_number
		elif mathematical_action_that_user_wants_to_take == '/': #code that will be executed if value of mathematical_action_that_user_wants_to_take is '/'
			if second_number !=0: #checking if second_number is not 0
				print(first_number / second_number) #output the result of division of first_number by second_number
			else: #code that will be executed if second_number equals to 0
				print("You can't divide by zero!") #print to user error message saying that division by 0 is impossible
	else: #code that will be executed if value of mathematical_action_that_user_wants_to_take is not - or + or / or *
		print('You have entered the wrong math action! Try again!') #print to user error message saying that he types wrong action			