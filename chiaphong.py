import random
with open('list.txt', 'r', encoding='utf-8') as f:
	lis = f.readlines()
	random.shuffle(lis)


sophong = 4
sohsphong = len(lis)//sophong # số học sinh mỗi phòng = tổng/số phòng = 22/4 = 5
#sorry 22/4 = 5 nha mình nhầm
#6 là số phòng bị dư

ds = [] #DS sau khi chia phong
i = 0
while len(lis)>0:
	try:
		ds.append([]) #Them phong
		for j in range(sohsphong):
			ds[i].append(lis[0])
			lis.pop(0)
		i+=1
	except:
		break

#Đoạn này lỗi
try:
	for i in range(len(ds[sophong])):
		ds[i].append(ds[sophong][0])
		ds[sophong].pop(0)
except:
	pass


for i in range(sophong):
	print(len(ds[i]))

for i in range(sophong):
	f = open(f'phong{i+1}.txt', 'w', encoding = 'utf-8')
	for j in range(sohsphong):
		f.write(ds[i][j])
	f.close()