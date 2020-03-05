""" index=0
score=[]


try:
    ssn = []
    while True:
        sn = input().strip()
        # sn = sys.stdin.readline().strip()
        #若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list。
        if sn == '':
            break
        sn = list(sn.split(" "))
        ssn.append(sn)
except:
    pass

while(index<len(ssn)):
	n=ssn[index]
	for i in range(0,n):
		score

	index+=n """

class Stu(object):
    def __init__(self,number,totalscore,chinese):
    	self.number=number
    	self.totalscore=totalscore
    	self.chinese=chinese
    @property
    def showtotal(self):
    	return self.totalscore

s=[]
t=[]
flag2=0
while True:
	Class=[]
	i=0
	j=0
	try:
		n=input().strip()
	except EOFError:
		break
	for i in range(int(n)):
		score=input().strip()
		score=score.split()
		total=0
		for j in range(3):
			total=total+int(score[j])
		Class.append(Stu(i+1,total,int(score[0])))
	Class.sort(key=lambda x:(-x.totalscore, -x.chinese, x.number))
	flag=0
	for Student in Class:
		if flag==5:
			break
		s.append(Student.number)
		t.append(Student.totalscore)
		flag=flag+1
	flag2=flag2+5
for f in range(0,flag2,1):
	if f%5==0 and f!=0:
		print()
	print(int(s[f]),int(t[f]))