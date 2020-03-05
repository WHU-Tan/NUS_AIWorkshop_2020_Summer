""" l=[]
r=[]
avg=[]
score_new=[]
number=[]
items=[]
d={}
read=[]
def dict_slice(ori_dict, start, end):
    slice_dict = {k: ori_dict[k] for k in list(ori_dict.keys())[start:end]}
    return slice_dict

line1=input()
line1=line1.split(" ")
n=int(line1[0])
k=int(line1[1])

name=input()
name=name.split(" ")

score=input()
score=score.split(" ")
for i in range(0,n):
    score_new.append(int(score[i]))

for i in range(0,n):
    d.setdefault(name[i],[]).append(score_new[i])


for i in range(0,k):
    read_num=input()
    read_num=read_num.split(" ")
    l.append(int(read_num[0])-1)
    r.append(int(read_num[1])-1)

for i in range(0,k):
    name_copy=list(d.keys())
    for item in name[l[i]:r[i]]:
        d_copy=dict_slice(d, l[i], r[i])
        if item in name_copy:
            avg.append(float(sum(d_copy[item])/(name.count(item))))
            name_copy.remove(item)
        else:
            continue
    print(float(sum(avg))/len(avg))
    avg=[] """

nk=input()
listnk=nk.split()
n=int(listnk[0])
k=int(listnk[1])

name=input()
listname=name.split()
sw1=set(listname)
sw2=' '.join(sw1)
unique=sw2.split()

score=input()
listscore=score.split()

x=0
flag=0
ave=[]
sum=0
for i in range(k):
	lr=input()
	listlr=lr.split()
	l=int(listlr[0])-1
	r=int(listlr[1])
	flag2=0
	sum=0
	for z in range(len(unique)): #every student
		x=0
		flag=0
		for y in range(l,r,1): #every score
			if listname[y]==unique[z]:
				x=x+int(listscore[y])
				flag=flag+1
		if flag!=0:
			flag2=flag2+1
			sum=sum+x/flag
	ave.append(round(sum/flag2,7))

for i in range(k):
	if isinstance(ave[i],int)==True:
		print(int(ave[i]))
	else:
		print(ave[i])