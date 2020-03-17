pi=3.1415927
inchToFoot=12
footToMile=5280
secondInHour=3600
revolution=1
diameters=[]
revolutions=[]
times=[]


while(revolution!=0):
    line=input()
    line=line.split(" ")
    revolution=int(line[1])

    diameters.append(float(line[0]))
    times.append(float(line[2]))
    revolutions.append(revolution)

for i in range(0,len(diameters)-1):
    distance=(diameters[i]*pi*revolutions[i])/(inchToFoot*footToMile)
    speed=distance/(times[i]/secondInHour)
    print(("Trip #%d: %.2f %.2f" %(i+1, distance, speed)))
    