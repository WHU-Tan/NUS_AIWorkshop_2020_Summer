art=input()
l=int(input())
kwrd=input()

wrd=art.split(" ")
del wrd[0:l]
cnt=wrd.count(kwrd)

print(cnt)