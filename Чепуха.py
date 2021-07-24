def one_way(r1,r2):
    if len(r1)==len(r2):
        return True
    for i in range(len(r1)):
        if r1[i]!=r2[i] and r1[:i]==r2[:i] and r1[i+1:]==r2[i+1:]:
            return True
qq=one_way('water','wafer')
print(qq)
        
        
        
   
      



