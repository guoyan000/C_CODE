list_a=[]
while True:
    n=input("请输入整数(输入q或者Q结束)：")
    if n=='q'or n=='Q':
        break
    m=int(n)
    list_a.append(m)
list_b=[x for x in list_a if x%2!=0]
print(list_b)