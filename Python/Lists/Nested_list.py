n = int(input())  # taking length from user
l = [] # creating list 
m =[]
for i in range(n):
       a = input()
       b = float(input())
       l.append([a,b])
       m.append(b)
m = sorted(set(m)) #unique sorted element
name = []
k = m[1]
for val in l:
     if k == val[1]:
        name.append(val[0])       
name.sort()
for j in name:
    print(j)  
