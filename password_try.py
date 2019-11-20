password = 'a123456'
trytime = 3

while trytime>0:
	pwd = input('請輸入密碼')
	if pwd == password:
		print('登入成功')
		trytime = 4 #讓while不成立
		break
	else:
		trytime = trytime-1
		if trytime == 0:
			print('沒機會了')
		else:
			print('密碼錯誤，還有', trytime ,'次機會' )

