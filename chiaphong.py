import random
with open('list.txt', 'r', encoding='utf-8') as f:
	lis = f.readlines()
	random.shuffle(lis)

sophong = 4
sohsphong = len(lis)//sophong

ds = []
i = 0
while len(lis)>0:
	try:
		ds.append([])
		for j in range(sohsphong):
			ds[i].append(lis[0])
			lis.pop(0)
		i+=1
	except:
		break

for i in range(len(ds[sophong])):
	ds[random.randint(0,sophong-1)].append(ds[sophong][0])
	ds[sophong].pop(0)

for i in range(sophong):
	f = open(f'phong{i+1}.txt', 'w', encoding = 'utf-8')
	for j in range(len(ds[i])):
		f.write(ds[i][j])
	f.close()
