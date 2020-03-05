""" a=[]

n=int(input())
num=input()
num=num.split(" ")
for i in range(0,n):
    a.append(int(num[i]))

dict={1:"     *\r     *\r     *\r     *\r     *\r     *\r     *  ",\
      0:"******\n*    *\n*    *\n*    *\n*    *\n*    *\n******  ",\
      2:"******\n     *\n     *\n******\n*     \n*     \n******  ",\
      3:"******\n     *\n     *\n******\n     *\n     *\n******  "}

for i in range(0,n):
    if a[i]==0:
        print(dict[0],)
    if a[i]==1:
        print(dict[1],)
    if a[i]==2:
        print(dict[2],)
    if a[i]==3:
        print(dict[3],) """

n=int(input())
num=input()
numlist=num.split()
if int(numlist[0])==0:
	line1='******'
	line2='*    *'
	line3='*    *'
	line4='*    *'
	line5='*    *'
	line6='*    *'
	line7='******'
elif int(numlist[0])==1:
	line1='     *'
	line2='     *'
	line3='     *'
	line4='     *'
	line5='     *'
	line6='     *'
	line7='     *'
elif int(numlist[0])==2:
	line1='******'
	line2='     *'
	line3='     *'
	line4='******'
	line5='*     '
	line6='*     '
	line7='******'
elif int(numlist[0])==3:
	line1='******'
	line2='     *'
	line3='     *'
	line4='******'
	line5='     *'
	line6='     *'
	line7='******'

for i in range(1,n,1):
	if int(numlist[i])==0:
		line1=line1+'  ******'
		line2=line2+'  *    *'
		line3=line3+'  *    *'
		line4=line4+'  *    *'
		line5=line5+'  *    *'
		line6=line6+'  *    *'
		line7=line7+'  ******'
	elif int(numlist[i])==1:
		line1=line1+'       *'
		line2=line2+'       *'
		line3=line3+'       *'
		line4=line4+'       *'
		line5=line5+'       *'
		line6=line6+'       *'
		line7=line7+'       *'
	elif int(numlist[i])==2:
		line1=line1+'  ******'
		line2=line2+'       *'
		line3=line3+'       *'
		line4=line4+'  ******'
		line5=line5+'  *     '
		line6=line6+'  *     '
		line7=line7+'  ******'
	elif int(numlist[i])==3:
		line1=line1+'  ******'
		line2=line2+'       *'
		line3=line3+'       *'
		line4=line4+'  ******'
		line5=line5+'       *'
		line6=line6+'       *'
		line7=line7+'  ******'
print(line1+'\n'+line2+'\n'+line3+'\n'+line4+'\n'+line5+'\n'+line6+'\n'+line7)