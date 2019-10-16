s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
s4=[1,2,3,4,5]
x=input("Enter student's name")
y=0

if(x==s1[0]):
    for no in s4:
        y+=s1[no]
    print( s1[0] +' '+str(y))
elif(x==s2[0]):
    for no in s4:
        y+=s2[no]
    print( s2[0] +' '+str(y) )
elif(x==s3[0]):
    for no in s4:
        y+=s3[no]
    print( s3[0] +' '+str(y))
else :
    print("Students is not recorded 0")        
