p1=input('k(amen),n(ojnisa),b(umaga)')
p2=input('k(amen),n(ojnisa),b(umaga)')
if (p1=='k' and p2=='b')or(p1=='n' and p2=='k')or(p1=='n' and p2=='b')or(p1=='b' and p2=='k'):
    print('vigral pervyi igrok')
elif (p2=='k' and p2=='b')or(p1=='n' and p2=='k')or(p1=='n' and p2=='b')or(p1=='b' and p2=='k'):
    print('vigral vtoroi igrok')
elif p1==p2:
    print('Nichya')
