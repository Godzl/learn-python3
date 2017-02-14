#杨辉三角
def triangles(max):#自定义最大列数
	L = [1]
	n = 0
	while n < max:
		yield L
		L.append(0)#在尾部追加0
		L = [L[i-1]+L[i] for i in range(len(L))]
		n = n + 1
		
#遇到yield时输出[1]
[1,0]此时i= 0,1
L = [L([-1]+L[0],L[0]+L[1]]即[1,1]
[1,1,0]此时i=0,1,2
L = [L[-1]+L[0],L[0]+L[1],L[1]+L[2]]即[1,2,1]
依次类推。