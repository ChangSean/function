#function 函式/功能

#function是用來【收納】程式碼的
#它是個功能

def washer(dry=False,water=8):
	print('加水',water,'分滿')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘衣')

washer(water=10)  #使用function

def say_hi():
	print('hello!')

say_hi()

def add(x,y):
	return x + y

result = add(3,4)
print(result)

def average(numbers):
	return sum(numbers) / len(numbers)

print(average([1,2,3]))
print(average([11,21,31]))