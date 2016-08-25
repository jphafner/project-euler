n=15
def euler300_adj(x,y,dx,dy,n,B,C,i,T,turnright):
   x+=dx
   y+=dy
   p=(x,y)
   neighbours=C[p]
   if neighbours not in T:
      T[neighbours]=[False,{}]
   if n==1:
      T[neighbours][0]=True
      return 1
   f=(x+dx,y+dy)
   l=(x-dy,y+dx)
   r=(x+dy,y-dx)
   bf=1<<i
   tryf= f not in B
   tryl= l not in B
   tryr= r not in B  
   if n>3:
      if tryf:
         C[f]+=bf
      if tryl:
         C[l]+=bf
      if tryr:
         C[r]+=bf
      B.add(p)
   T2=T[neighbours][1]
   t=0
   if tryf:
      t+=euler300_adj(x,y,dx,dy,n-1,B,C,i+1,T2,turnright)
   if tryl and not turnright:
      t+=euler300_adj(x,y,-dy,dx,n-1,B,C,i+1,T2,False)
   if tryr:
      t+=euler300_adj(x,y,dy,-dx,n-1,B,C,i+1,T2,False)
   if n>3:
      if tryf:
         C[f]-=bf
      if tryl:
         C[l]-=bf
      if tryr:
         C[r]-=bf
      B.remove(p)
   if t: T[neighbours][0]=True
   return t
tree={}
C=defaultdict(int)
C[(0,1)]=1 
euler300_adj(0,1,0,-1,n,set(),C,0,tree,True)
 
best2=[0]*2**n
def euler300_search(i,n,T,A,N):
   for bf,(valid,T2) in T.items():
      if not valid: continue
      if n==1:
         for j in xrange(i-1):
            if bf&(1<<j):
               test=(1<<i)+(1<<j)
               for k in xrange(2**N):
                  if (k&test)==test:
                     v=A[k]+1
                     if v>best2[k]: best2[k]=v
         return
      for j in xrange(i-1):
         if bf&(1<<j):
            test=(1<<i)+(1<<j)
            for k in xrange(2**N):
               if (k&test)==test:
                  v=A[k]+1
                  A[k]=v
                  if v>best2[k]: best2[k]=v
      euler300_search(i+1,n-1,T2,A,N)
      for j in xrange(i-1):
         if bf&(1<<j):
            test=(1<<i)+(1<<j)
            for k in xrange(2**N):
               if (k&test)==test:
                  A[k]-=1
euler300_search(0,n,tree,[0]*2**n,n)
t=0
for k in xrange(2**n):
   for i in xrange(n-1):
      if ((k>>i)&3)==3: best2[k]+=1
   t+=best2[k]
print t


#!/usr/bin/python
#
# Project Euler Problem 300
 
# First generate all possible foldings of a protein of length 15.
todo=[[(0,0),(0,1)]]
for i in range(13):
  newdo=[]
  for c in todo:
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
      newnode=(c[-1][0]+dx,c[-1][1]+dy)
      if newnode not in c:
        newdo.append(c+[newnode])
  todo=newdo
 
# Then generate adjacency lists for each one and only keep the unique lists
# Use dictionaries to do the uniqueness checking for me, and use separate
# dictionaries for each length to do the sorting in advance, too.
adj=[{},{},{},{},{},{},{},{},{}]
for c in todo:
  al=[]
  for i in range(13):
    #only proteins an odd distance apart can be adjacent, and ignore
    #adjacencies of distance 1; they will be adjacent in ANY folding
    for j in range(i+3,15,2): 
      dx=abs(c[i][0]-c[j][0])
      dy=abs(c[i][1]-c[j][1])
      if dx+dy==1:
        #note that these always get appended in order, so there is no need
        #to sort this list later
        al.append((i,j))
  alt=tuple(al)
  adj[len(alt)][alt]=True
 
# Now check each protein against the list.
totadj=0
for p1 in "HP":
 for p2 in "HP":
  for p3 in "HP":
   for p4 in "HP":
    for p5 in "HP":
     for p6 in "HP":
      for p7 in "HP":
       for p8 in "HP":
        for p9 in "HP":
         for p10 in "HP":
          for p11 in "HP":
           for p12 in "HP":
            for p13 in "HP":
             for p14 in "HP":
              for p15 in "HP":
                p=p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14+p15
                #count forced adjacencies
                for i in range(14):
                  if p[i]=="H" and p[i+1]=="H":
                    totadj+=1
                maxadj=0
                for k in range(8,1,-1):
                  if maxadj>k:
                    break
                  for c in adj[k].keys():
                    ca=0
                    for pr in c:
                      if p[pr[0]]=="H" and p[pr[1]]=="H":
                        ca+=1
                    if ca>maxadj:
                      maxadj=ca
                      if maxadj==k:
                        break
                totadj+=maxadj
print totadj,"total adjacencies for 32768 cases"
avs=repr(totadj*5**15)
print avs[:-15]+"."+avs[-15:],"average adjacencies"
