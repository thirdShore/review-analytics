data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))

print('档案读取完了，总共有',len(data),'条留言')
#print('\n', data[0])
#print('---------------------')
#print(data[1])
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均长度为',sum_len / len(data))