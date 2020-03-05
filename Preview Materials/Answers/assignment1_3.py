t=int(input())

out=[]

#test
for i in range(0,t):
    from queue import Queue
    n=int(input())
    q=Queue(n)
    q.queue.clear()
    for i in range(0,n):
        opera=input()
        if(opera=="Count"):
            out.append(q.qsize())
        if(opera=="Out"):
            if(q.empty()!=True):
                out.append(q.get())
            else:
                out.append(-1)
        if(opera!="Count" and opera!="Out"):
            opera_new=opera.split(" ")
            num=int(opera_new[1])
            q.put(num)

for item in out:
    print(item)