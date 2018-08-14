width = input('请输入体重，单位kg:')
height = input('请输入身高，单位cm:')

bmi = int(width) / pow(float(height)/100,2)
print('BMI = ' + str(bmi))

if bmi < 18.5:
	print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
	print('死胖子')