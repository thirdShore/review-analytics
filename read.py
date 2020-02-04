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

#清单的筛选
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有',len(new),'条留言长度小于100')
print(new[0])
print(new[1])

# reviews incloude good
good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'条留言提到good')
print(good[0])