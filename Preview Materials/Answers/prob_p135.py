def calculation(number,digit):
    remainder=0
    summary=0
    while(number!=0):
        remainder=int(number%digit)
        number=int(number/digit)
        summary=int(summary+remainder)
    return summary

sumDec=0
sumDuo=0
sumHex=0

for i in range(2992,9999,1):
    sumDec=calculation(i,10)
    sumDuo=calculation(i,12)
    sumHex=calculation(i,16)
    if((sumDec==sumDuo) and (sumDuo==sumHex)):
        print(i)