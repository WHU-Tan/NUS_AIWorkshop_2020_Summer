def cut_text(text,lenth):
    n=int(len(text)/lenth)
    textCut=[]
    for i in range(0,n):
        textCut.append(text[i*lenth:(i+1)*lenth])
    return textCut

def StringToChar(string):
    n=len(string)
    chars=[]
    for i in range(0,n):
        chars.append(string[i])
    return chars

def Decoding(keyword,ciphertext):
    columnLength=len(keyword)
    rowLength=int(len(ciphertext)/columnLength)
    text=[]
    numbers=[]
    keywordTemp=StringToChar(keyword)

    for i in range(0,columnLength):
        numbers.append(i)
    
    keyList=list(zip(keywordTemp,numbers))
    keySorted=sorted(keyList, key=lambda x:x[0])

    textCutoff=cut_text(ciphertext,rowLength)

    finalKey=[x[1] for x in keySorted]
    newList = list(zip(finalKey, textCutoff))

    finalList=sorted(newList, key=lambda x:x[0])

    textSorted=[x[1] for x in finalList]
    for i in range(0,rowLength):
        for j in range(0,columnLength):
            text.append(textSorted[j][i])
    finalText="".join(text)
    print(finalText)

inputs = []
while True:
    inputLine=input()
    if(inputLine!='THEEND'):
        inputs.append(inputLine)
    else:
        break

for i in range(0, len(inputs),2):
    keyword=inputs[i]
    ciphertext=inputs[i+1]
    Decoding(keyword,ciphertext)