password = 'a123456'

n = 3
while n > 0:
	n = n - 1
	enter = input('enter your password:')
	if enter == password:
		print('login!')
		break
	else:
		print('wrong!')
		if n > 0:
			print(n, 'times left')
		else:
			print('your account is blocked')