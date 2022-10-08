#list(int)->str
a=[1,2,3]
s=''.join(map(str,a))
print(s)

#list(int)->int
a=[1,2,3]
s=''.join(map(str,a))
a=int(s)
print(a)

#list(str)->str
s=['1','2','3']
s=''.join(s)    #join针对str类型
print(s)

#list(str)->int
s=['1','2','3']
s=''.join(s)
a=int(s)
print(a)

#list(str)->list(int)
s=['1','2','3']
a=list(map(int,s))
print(a)

#list(int)->list(str)
a=[1,2,3]
s=list(map(str,a))


#总结：
#转基本类型用join，str直接用,int要map(str,a)
#转列表用list(map(基本类型，数组名))

