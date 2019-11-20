password = 'a123456'
trytime = 3

while trytime>0:
	pwd = input('請輸入密碼')
	print(pwd)
	if pwd == password:
		print('登入成功')
		trytime = 4
		break
	else:
		trytime = trytime-1
		print('密碼錯誤，還有', trytime ,'次機會' )

