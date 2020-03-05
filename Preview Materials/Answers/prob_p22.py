score=input()
score_new=score.split(" ")
a=int(score_new[0])
b=int(score_new[1])
c=int(score_new[2])
if(a>=60 and (c>=60 or b>=60)):
    print('True')
else:
    print('False')