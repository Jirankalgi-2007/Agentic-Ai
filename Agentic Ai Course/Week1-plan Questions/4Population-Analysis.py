#A certain town has population 80,000. out of total population 54% are men and out of total men 85% are literate.
#out of total women 11% are illiterate.
#Calculate and print the count of total men, total women, literate men, literate women, illiterate men and
#illiterate women.

p=80000
m=80000*(54/100)
liM=m*(85/100)
iliM=m-liM
w=80000-m
iliW=w*(11/100)
liW=w-iliW

print("Total Men : ",m)
print("Total Women : ",w)
print("Total Literate Men : ",liM)
print("Total Literate Women : ",liW)
print("Total Illiterate Men : ",iliM)
print("Total Illiterate Women : ",iliW)
