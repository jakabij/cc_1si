array=[0,1]
sum=0
for i in range(2,31):
	array.append(array[i-1]+sum)
	sum=array[i-1]

for i in range(30):
	print("%d:" %(i+1),array[i])
