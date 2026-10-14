#1.apple is red and sweet fruit
#['si', 'dna', 'tiurf', 'elppa', 'der', 'teews']
'''
n=input().split()
l=[]
for i in n:
    l+=[i[::-1]]    
even=l[::2]
odd=l[1::2]
print(odd + even)
'''
'''
n=input().split()
odd=[]
even=[]
for i in range(len(n)):
    if i%2!=0:
        odd+=[n[i][::-1]]
    else:
        even+=[n[i][::-1]]
print(odd+even)        
'''
for i in range(1,6):
    print(i, end=' ')
