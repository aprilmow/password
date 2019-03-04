password = 'a123456'

n = 3
while True:
	enter = input('enter your password:')
	if enter == password:
		print('login!')
		break
	else:
		n = n - 1
		print('wrong!', n, 'times left')
		if n == 0:
			break