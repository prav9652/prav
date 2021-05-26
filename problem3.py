import math
def validate(i):
    #print("Valding"+i)
    if(i[0].isupper() and i[1:].isnumeric() and int(i[1:])>=1 and int(i[1:])<=26):
        return True
    print('Bad reference: '+i)
    return False

def distance(p1,p2):
    X=(ord(p1[0])-64,int(p1[1:]))
    Y=(ord(p2[0])-64,int(p2[1:]))
    return math.sqrt((X[0]-Y[0])**2+(X[1]-Y[1])**2)
st=input("Enter trip map references: ").split()
flag=True
totalDist=0
for i in range(len(st)-1):
	if validate(st[i]) and validate(st[i+1]):
	    totalDist+=distance(st[i],st[i+1])
	else:
	    flag=False
	    break
if(flag):
    print(str(round(totalDist*0.5,1))+" km")