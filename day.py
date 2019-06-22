def leap_year(year):
	if((year%4==0)&(year%100!=0)|(year%400==0)):
		return 'leap year'
	else:
		return 'normal year'

def sum_day(year, month, day):
	sumday = 0
	for i in range(1, year):
		if leap_year(i)=='normal year':
			sumday += 365
		else :
			sumday += 366
	for i in range(1, month):
		if i==1 or i==3 or i==5 or i==7 or i==8 or i==10:
			sumday += 31
		elif i==2:
			if leap_year(year)=='normal year':
				sumday += 28
			else :
				sumday += 29
		else :
			sumday += 30
	sumday += day
	return sumday

def print_day(year, month, day, x):
	days = ('日曜日', '月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日')
	print(f'{year}年{month}月{day}日は{days[x]}です')

print("____年__月__日？'ex.)2019 5 1'")
year, month, day = (int(n) for n in input().split())
x = sum_day(year, month, day)%7
print_day(year, month, day, x)
